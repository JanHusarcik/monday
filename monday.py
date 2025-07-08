import os
import sys
from pprint import pp
from pathlib import Path
from typing import List, Final, Dict, Optional, Tuple
from sgqlc.operation import Operation
from monday_schema import monday_schema as schema
from sgqlc.endpoint.http import HTTPEndpoint
from alive_progress import alive_bar
import structlog
import json
from dotenv import load_dotenv
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from termcolor import colored

def get_env(file: Optional[str] = None) -> Tuple[str, str]:
    load_dotenv(dotenv_path=file)
    if (api_key := os.getenv("API_KEY")) is None or (base_url := os.getenv("BASE_URL")) is None:
        print("Please set the environment variables API_KEY and BASE_URL.\nYou can do so by creating `.env` file in the same folder as you run this script.")
        sys.exit(1)
    return api_key, base_url


def create_log(filename: str = "toolkit") -> structlog.BoundLogger:
    structlog.configure(
        # wrapper_class=structlog.make_filtering_bound_logger(INFO),
        processors=[
            structlog.processors.TimeStamper(fmt="ISO", utc=True),
            structlog.processors.add_log_level,
            # add_func_name,
            structlog.processors.EventRenamer("msg"),
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(
                ensure_ascii=False, sort_keys=True),  # has to be last in the list
        ],
        logger_factory=structlog.WriteLoggerFactory(
            file=Path(filename).with_suffix(".jsonl").open("wt", encoding="utf-8")),
    )
    return structlog.get_logger()


def get_items_list(endpoint: HTTPEndpoint, board: int, log: structlog.BoundLogger) -> List[int]:
    with alive_bar(title="Listing items",  enrich_print=False) as bar:
        # get first page
        op = Operation(schema.Query)
        items_list: List[int] = []
        items_page = op.boards(ids=[board]).items_page()
        items_page.cursor()
        items_page.items.id()
        data = endpoint(op)
        items_list.extend(
            int(item['id']) for item in data['data']['boards'][0]['items_page']['items'])
        cursor = data['data']['boards'][0]['items_page']['cursor']
        bar.title = f"Listing items {cursor}"
        bar()
        # get the rest of the pages
        while True:
            op = Operation(schema.Query)
            next_items_page = op.next_items_page(cursor=cursor, limit=500)
            next_items_page.cursor()
            next_items_page.items.id()

            data = endpoint(op)
            if (cursor := data['data']['next_items_page']['cursor']) is None:
                break

            if data['data']['next_items_page']['items'] == []:
                break
            items_list.extend(int(item['id'])
                              for item in data['data']['next_items_page']['items'])
            bar.title = f"Listing items {cursor}"
            bar()
    return items_list


def save_item(item_id: int, data: Dict) -> None:
    with open(os.path.join("data", str(item_id)+".json"), "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


def get_item(endpoint: HTTPEndpoint, item_id: int, log: structlog.BoundLogger) -> None:
    op = Operation(schema.Query)
    item = op.items(ids=[item_id])
    item.__fields__('id', 'created_at', 'creator_id', 'email',
                    'name', 'relative_link', 'state', 'updated_at', 'url')
    item.parent_item.id()
    item.subitems.id()
    item.assets.id()
    item.assets.url()
    item.group.id()
    item.group.title()
    item.column_values.__fields__('id', 'text', 'type', 'value')
    item.column_values.column.__fields__(
        'archived', 'description', 'id', 'settings_str', 'title', 'type', 'width')
    data = endpoint(op)
    save_item(item_id, data['data']['items'][0])


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments for the script.

    Returns:
        argparse.Namespace: Parsed arguments containing the project UID.
    """
    parser = argparse.ArgumentParser(
        description="Download all items from a Monday.com board.")
    parser.add_argument("board", help="Board id")
    return parser.parse_args()


def main():
    api_key, url = get_env()
    headers: Final[Dict[str, str]] = {'Authorization': api_key}
    endpoint = HTTPEndpoint(url, headers)
    os.system("cls") if sys.stdout.isatty() else None
    log = create_log("copy_comments")
    args = parse_args()
    log.info("Starting to copy comments from monday.com",
             board=args.board, url=url)
    try:
        items_list = get_items_list(endpoint, args.board, log)
        log.info("Items list fetched", count=len(items_list))
        os.makedirs("data", exist_ok=True)
        with alive_bar(title="Downloading items", enrich_print=False, total=len(items_list)) as bar:
        #     for item in items_list:
        #         get_item(endpoint, item, log)
        #         bar()

            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(get_item, endpoint, item, log) for item in items_list]
                try:
                    for future in as_completed(futures):
                        bar()
                except KeyboardInterrupt:
                    print(colored("\nOperation cancelled by user.", 'yellow'))
                    executor.shutdown(wait=False, cancel_futures=True)
                    return
    except KeyboardInterrupt:
        print(colored("\nOperation cancelled by user.", 'yellow'))
        return
    except Exception as e:
        log.exception("An error occurred while processing items")
        print(colored(f"An error occurred: {e}", 'red'))
        sys.exit(1)


if __name__ == '__main__':
    main()
