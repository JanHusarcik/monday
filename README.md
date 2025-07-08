# Monday.com Board Item Downloader

This project is a Python tool for downloading all items from a specified [Monday.com](https://monday.com) board. It retrieves item data using the Monday.com GraphQL API and saves each item as a JSON file in a local `data/` directory. The tool supports efficient parallel downloading and provides progress feedback in the terminal.

## Features

- Downloads all items from a given Monday.com board.
- Saves each item as a separate JSON file.
- Uses up to 5 parallel workers for faster downloads.
- Progress bars for listing and downloading items.
- Structured logging to a JSONL file.
- Command-line interface.
- Environment variable configuration.

## Requirements

[uv](https://docs.astral.sh/uv/getting-started/installation/) An extremely fast Python package and project manager, written in Rust.

`uv` would take care of installing the required packages and managing the environment.

- Python 3.8+
- A Monday.com API key and base URL.
- The following Python packages:
  - `sgqlc`
  - `alive-progress`
  - `structlog`
  - `python-dotenv`
  - `termcolor`


## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Create a `.env` file** in the project root with the following content:

```
API_KEY=your_monday_api_key
BASE_URL=https://api.monday.com/v2    
```

3. **Ensure the `data/` directory exists** (it will be created automatically if not).

## Usage

Run the script from the command line, providing the board ID as an argument:


Example:

```bash
uv run monday.py 4457216800
```

- All items will be saved as individual JSON files in the `data/` directory.
- Logs are written to `copy_comments.jsonl`.

## Logging

- Logs are structured and saved in JSONL format for easy analysis.
- Errors and progress are also printed to the terminal.

## Notes

- The script uses up to 5 threads to download items in parallel.
- If you interrupt the script (Ctrl+C), it will exit gracefully.
- Make sure your API key has sufficient permissions to access the board.

---

*For any issues or feature requests, please open an issue on the repository.*

