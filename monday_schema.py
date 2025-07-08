import sgqlc.types
import sgqlc.types.datetime


monday_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class ActivateUsersErrorCode(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('CANNOT_UPDATE_SELF', 'EXCEEDS_BATCH_LIMIT', 'FAILED', 'INVALID_INPUT', 'USER_NOT_FOUND')


class AssetsSource(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('all', 'columns', 'gallery')


class AssignTeamOwnersErrorCode(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('CANNOT_UPDATE_SELF', 'EXCEEDS_BATCH_LIMIT', 'FAILED', 'INVALID_INPUT', 'USER_NOT_FOUND', 'USER_NOT_MEMBER_OF_TEAM', 'VIEWERS_OR_GUESTS')


class BaseRoleName(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('ADMIN', 'GUEST', 'MEMBER', 'VIEW_ONLY')


class BoardAttributes(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('communication', 'description', 'name')


class BoardKind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('private', 'public', 'share')


class BoardObjectType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('board', 'custom_object', 'document', 'sub_items_board')


class BoardSubscriberKind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('owner', 'subscriber')


class BoardsOrderBy(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('created_at', 'used_at')


Boolean = sgqlc.types.Boolean

class ColumnProperty(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('description', 'title')


class ColumnType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('auto_number', 'board_relation', 'button', 'checkbox', 'color_picker', 'country', 'creation_log', 'date', 'dependency', 'direct_doc', 'doc', 'dropdown', 'email', 'file', 'formula', 'group', 'hour', 'integration', 'item_assignees', 'item_id', 'last_updated', 'link', 'location', 'long_text', 'mirror', 'name', 'numbers', 'people', 'person', 'phone', 'progress', 'rating', 'status', 'subtasks', 'tags', 'team', 'text', 'time_tracking', 'timeline', 'unsupported', 'vote', 'week', 'world_clock')


class CompareValue(sgqlc.types.Scalar):
    __schema__ = monday_schema


class CustomActivityColor(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('BRINK_PINK', 'CELTIC_BLUE', 'CORNFLOWER_BLUE', 'DINGY_DUNGEON', 'GO_GREEN', 'GRAY', 'LIGHT_DEEP_PINK', 'LIGHT_HOT_PINK', 'MAYA_BLUE', 'MEDIUM_TURQUOISE', 'PARADISE_PINK', 'PHILIPPINE_GREEN', 'PHILIPPINE_YELLOW', 'SLATE_BLUE', 'VIVID_CERULEAN', 'YANKEES_BLUE', 'YELLOW_GREEN', 'YELLOW_ORANGE')


class CustomActivityIcon(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('ASCENDING', 'CAMERA', 'CONFERENCE', 'FLAG', 'GIFT', 'HEADPHONES', 'HOMEKEYS', 'LOCATION', 'NOTEBOOK', 'PAPERPLANE', 'PLANE', 'PLIERS', 'TRIPOD', 'TWOFLAGS', 'UTENCILS')


Date = sgqlc.types.datetime.Date

class DeactivateUsersErrorCode(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('CANNOT_UPDATE_SELF', 'EXCEEDS_BATCH_LIMIT', 'FAILED', 'INVALID_INPUT', 'USER_NOT_FOUND')


class DiscountPeriod(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('MONTHLY', 'YEARLY')


class DocBlockContentType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('bulleted_list', 'check_list', 'code', 'divider', 'image', 'large_title', 'layout', 'medium_title', 'normal_text', 'notice_box', 'numbered_list', 'page_break', 'quote', 'small_title', 'table', 'video')


class DocsOrderBy(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('created_at', 'used_at')


class DuplicateBoardType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('duplicate_board_with_pulses', 'duplicate_board_with_pulses_and_updates', 'duplicate_board_with_structure')


class File(sgqlc.types.Scalar):
    __schema__ = monday_schema


class FileColumnValue(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('asset', 'box', 'doc', 'dropbox', 'google_drive', 'link', 'onedrive')


class FileLinkValueKind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('box', 'dropbox', 'google_drive', 'link', 'onedrive')


class FirstDayOfTheWeek(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('monday', 'sunday')


Float = sgqlc.types.Float

class FolderColor(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('AQUAMARINE', 'BRIGHT_BLUE', 'BRIGHT_GREEN', 'CHILI_BLUE', 'DARK_ORANGE', 'DARK_PURPLE', 'DARK_RED', 'DONE_GREEN', 'INDIGO', 'LIPSTICK', 'NULL', 'PURPLE', 'SOFIA_PINK', 'STUCK_RED', 'SUNSET', 'WORKING_ORANGE')


class FolderCustomIcon(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('FOLDER', 'MOREBELOW', 'MOREBELOWFILLED', 'NULL', 'WORK')


class FolderFontWeight(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('FONT_WEIGHT_BOLD', 'FONT_WEIGHT_LIGHT', 'FONT_WEIGHT_NORMAL', 'FONT_WEIGHT_VERY_LIGHT', 'NULL')


class GroupAttributes(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('color', 'position', 'relative_position_after', 'relative_position_before', 'title')


class HostType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('ACCOUNT', 'APP_FEATURE_OBJECT', 'BOARD')


ID = sgqlc.types.ID

class ISO8601DateTime(sgqlc.types.Scalar):
    __schema__ = monday_schema


Int = sgqlc.types.Int

class InviteUsersErrorCode(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('ERROR',)


class ItemsOrderByDirection(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('asc', 'desc')


class ItemsQueryOperator(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('and', 'or')


class ItemsQueryRuleOperator(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('any_of', 'between', 'contains_terms', 'contains_text', 'ends_with', 'greater_than', 'greater_than_or_equals', 'is_empty', 'is_not_empty', 'lower_than', 'lower_than_or_equal', 'not_any_of', 'not_contains_text', 'starts_with', 'within_the_last', 'within_the_next')


class JSON(sgqlc.types.Scalar):
    __schema__ = monday_schema


class Kind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('person', 'team')


class ManagedColumnState(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('active', 'deleted', 'inactive')


class ManagedColumnTypes(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('dropdown', 'status')


class NotificationTargetType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('Post', 'Project')


class NumberValueUnitDirection(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('left', 'right')


class PositionRelative(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('after_at', 'before_at')


class Product(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('crm', 'dev', 'forms', 'knowledge', 'service', 'whiteboard', 'work_management', 'workflows')


class RemoveTeamOwnersErrorCode(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('CANNOT_UPDATE_SELF', 'EXCEEDS_BATCH_LIMIT', 'FAILED', 'INVALID_INPUT', 'USER_NOT_FOUND', 'USER_NOT_MEMBER_OF_TEAM', 'VIEWERS_OR_GUESTS')


class State(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('active', 'all', 'archived', 'deleted')


class StatusColumnColors(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('american_gray', 'aquamarine', 'berry', 'blackish', 'bright_blue', 'bright_green', 'brown', 'bubble', 'chili_blue', 'coffee', 'dark_blue', 'dark_indigo', 'dark_orange', 'dark_purple', 'dark_red', 'done_green', 'egg_yolk', 'explosive', 'grass_green', 'indigo', 'lavender', 'lilac', 'lipstick', 'navy', 'orchid', 'peach', 'pecan', 'purple', 'river', 'royal', 'saladish', 'sky', 'sofia_pink', 'steel', 'stuck_red', 'sunset', 'tan', 'teal', 'winter', 'working_orange')


String = sgqlc.types.String

class SubscriptionDiscountModelType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('nominal', 'percent')


class SubscriptionDiscountType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('one_time', 'recurring')


class SubscriptionPeriodType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('monthly', 'yearly')


class SubscriptionStatus(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('active', 'inactive')


class UpdateEmailDomainErrorCode(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('CANNOT_UPDATE_SELF', 'EXCEEDS_BATCH_LIMIT', 'FAILED', 'INVALID_INPUT', 'UPDATE_EMAIL_DOMAIN_ERROR', 'USER_NOT_FOUND')


class UpdateUserAttributesErrorCode(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('INVALID_FIELD',)


class UpdateUsersRoleErrorCode(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('CANNOT_UPDATE_SELF', 'EXCEEDS_BATCH_LIMIT', 'FAILED', 'INVALID_INPUT', 'USER_NOT_FOUND')


class UserKind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('all', 'guests', 'non_guests', 'non_pending')


class UserRole(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('ADMIN', 'GUEST', 'MEMBER', 'VIEW_ONLY')


class VersionKind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('current', 'deprecated', 'dev', 'maintenance', 'old__maintenance', 'old_previous_maintenance', 'previous_maintenance', 'release_candidate')


class WebhookEventType(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('change_column_value', 'change_name', 'change_specific_column_value', 'change_status_column_value', 'change_subitem_column_value', 'change_subitem_name', 'create_column', 'create_item', 'create_subitem', 'create_subitem_update', 'create_update', 'delete_update', 'edit_update', 'item_archived', 'item_deleted', 'item_moved_to_any_group', 'item_moved_to_specific_group', 'item_restored', 'move_subitem', 'subitem_archived', 'subitem_deleted')


class WorkflowBlockKind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('WAIT',)


class WorkflowVariableSourceKind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('host_metadata', 'node_results', 'reference', 'user_config')


class WorkspaceKind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('closed', 'open', 'template')


class WorkspaceSubscriberKind(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('owner', 'subscriber')


class WorkspacesOrderBy(sgqlc.types.Enum):
    __schema__ = monday_schema
    __choices__ = ('created_at',)


class policy__Policy(sgqlc.types.Scalar):
    __schema__ = monday_schema



########################################################################
# Input Objects
########################################################################
class ColumnMappingInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('source', 'target')
    source = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='source')
    target = sgqlc.types.Field(ID, graphql_name='target')


class CreateDocBoardInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('column_id', 'item_id')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='column_id')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='item_id')


class CreateDocInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('board', 'workspace')
    board = sgqlc.types.Field(CreateDocBoardInput, graphql_name='board')
    workspace = sgqlc.types.Field('CreateDocWorkspaceInput', graphql_name='workspace')


class CreateDocWorkspaceInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('folder_id', 'kind', 'name', 'workspace_id')
    folder_id = sgqlc.types.Field(ID, graphql_name='folder_id')
    kind = sgqlc.types.Field(BoardKind, graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    workspace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workspace_id')


class CreateDropdownColumnSettingsInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('labels',)
    labels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateDropdownLabelInput'))), graphql_name='labels')


class CreateDropdownLabelInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('label',)
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')


class CreateStatusColumnSettingsInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('labels',)
    labels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateStatusLabelInput'))), graphql_name='labels')


class CreateStatusLabelInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('label', 'color', 'index', 'description', 'is_done')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    color = sgqlc.types.Field(sgqlc.types.non_null(StatusColumnColors), graphql_name='color')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_done = sgqlc.types.Field(Boolean, graphql_name='is_done')


class CreateTeamAttributesInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('name', 'is_guest_team', 'parent_team_id', 'subscriber_ids')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_guest_team = sgqlc.types.Field(Boolean, graphql_name='is_guest_team')
    parent_team_id = sgqlc.types.Field(ID, graphql_name='parent_team_id')
    subscriber_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='subscriber_ids')


class CreateTeamOptionsInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('allow_empty_team',)
    allow_empty_team = sgqlc.types.Field(Boolean, graphql_name='allow_empty_team')


class FileInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('asset_id', 'file_type', 'link_to_file', 'name', 'object_id')
    asset_id = sgqlc.types.Field(ID, graphql_name='assetId')
    file_type = sgqlc.types.Field(sgqlc.types.non_null(FileColumnValue), graphql_name='fileType')
    link_to_file = sgqlc.types.Field(String, graphql_name='linkToFile')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    object_id = sgqlc.types.Field(ID, graphql_name='objectId')


class GrantMarketplaceAppDiscountData(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('days_valid', 'discount', 'is_recurring', 'period', 'app_plan_ids')
    days_valid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='days_valid')
    discount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='discount')
    is_recurring = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='is_recurring')
    period = sgqlc.types.Field(DiscountPeriod, graphql_name='period')
    app_plan_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='app_plan_ids')


class ItemsPageByColumnValuesQuery(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('column_id', 'column_values')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='column_id')
    column_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='column_values')


class ItemsQuery(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('groups', 'ids', 'operator', 'order_by', 'rules')
    groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ItemsQueryGroup')), graphql_name='groups')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')
    operator = sgqlc.types.Field(ItemsQueryOperator, graphql_name='operator')
    order_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ItemsQueryOrderBy')), graphql_name='order_by')
    rules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ItemsQueryRule')), graphql_name='rules')


class ItemsQueryGroup(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('rules', 'groups', 'operator')
    rules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ItemsQueryRule')), graphql_name='rules')
    groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ItemsQueryGroup')), graphql_name='groups')
    operator = sgqlc.types.Field(ItemsQueryOperator, graphql_name='operator')


class ItemsQueryOrderBy(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('column_id', 'direction')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='column_id')
    direction = sgqlc.types.Field(ItemsOrderByDirection, graphql_name='direction')


class ItemsQueryRule(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('column_id', 'compare_value', 'compare_attribute', 'operator')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='column_id')
    compare_value = sgqlc.types.Field(sgqlc.types.non_null(CompareValue), graphql_name='compare_value')
    compare_attribute = sgqlc.types.Field(String, graphql_name='compare_attribute')
    operator = sgqlc.types.Field(ItemsQueryRuleOperator, graphql_name='operator')


class PaginationInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('limit', 'last_id')
    limit = sgqlc.types.Field(Int, graphql_name='limit')
    last_id = sgqlc.types.Field(Int, graphql_name='lastId')


class TimelineItemTimeRange(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('start_timestamp', 'end_timestamp')
    start_timestamp = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='start_timestamp')
    end_timestamp = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='end_timestamp')


class UpdateDropdownColumnSettingsInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('labels',)
    labels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdateDropdownLabelInput'))), graphql_name='labels')


class UpdateDropdownLabelInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('label', 'id', 'is_deactivated')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    id = sgqlc.types.Field(Int, graphql_name='id')
    is_deactivated = sgqlc.types.Field(Boolean, graphql_name='is_deactivated')


class UpdateEmailDomainAttributesInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('user_ids', 'new_domain')
    user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids')
    new_domain = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='new_domain')


class UpdateStatusColumnSettingsInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('labels',)
    labels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdateStatusLabelInput'))), graphql_name='labels')


class UpdateStatusLabelInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('label', 'color', 'index', 'description', 'is_done', 'id', 'is_deactivated')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    color = sgqlc.types.Field(sgqlc.types.non_null(StatusColumnColors), graphql_name='color')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_done = sgqlc.types.Field(Boolean, graphql_name='is_done')
    id = sgqlc.types.Field(Int, graphql_name='id')
    is_deactivated = sgqlc.types.Field(Boolean, graphql_name='is_deactivated')


class UpdateWorkspaceAttributesInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('description', 'kind', 'name')
    description = sgqlc.types.Field(String, graphql_name='description')
    kind = sgqlc.types.Field(WorkspaceKind, graphql_name='kind')
    name = sgqlc.types.Field(String, graphql_name='name')


class UserAttributesInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('birthday', 'email', 'join_date', 'name', 'location', 'mobile_phone', 'phone', 'title', 'department')
    birthday = sgqlc.types.Field(String, graphql_name='birthday')
    email = sgqlc.types.Field(String, graphql_name='email')
    join_date = sgqlc.types.Field(String, graphql_name='join_date')
    name = sgqlc.types.Field(String, graphql_name='name')
    location = sgqlc.types.Field(String, graphql_name='location')
    mobile_phone = sgqlc.types.Field(String, graphql_name='mobile_phone')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    title = sgqlc.types.Field(String, graphql_name='title')
    department = sgqlc.types.Field(String, graphql_name='department')


class UserUpdateInput(sgqlc.types.Input):
    __schema__ = monday_schema
    __field_names__ = ('user_id', 'user_attribute_updates')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='user_id')
    user_attribute_updates = sgqlc.types.Field(sgqlc.types.non_null(UserAttributesInput), graphql_name='user_attribute_updates')



########################################################################
# Output Objects and Interfaces
########################################################################
class ColumnValue(sgqlc.types.Interface):
    __schema__ = monday_schema
    __field_names__ = ('column', 'id', 'text', 'type', 'value')
    column = sgqlc.types.Field(sgqlc.types.non_null('Column'), graphql_name='column')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    text = sgqlc.types.Field(String, graphql_name='text')
    type = sgqlc.types.Field(sgqlc.types.non_null(ColumnType), graphql_name='type')
    value = sgqlc.types.Field(JSON, graphql_name='value')


class Account(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('active_members_count', 'country_code', 'first_day_of_the_week', 'id', 'logo', 'name', 'plan', 'products', 'show_timeline_weekends', 'sign_up_product_kind', 'slug', 'tier')
    active_members_count = sgqlc.types.Field(Int, graphql_name='active_members_count')
    country_code = sgqlc.types.Field(String, graphql_name='country_code')
    first_day_of_the_week = sgqlc.types.Field(sgqlc.types.non_null(FirstDayOfTheWeek), graphql_name='first_day_of_the_week')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    logo = sgqlc.types.Field(String, graphql_name='logo')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    plan = sgqlc.types.Field('Plan', graphql_name='plan')
    products = sgqlc.types.Field(sgqlc.types.list_of('AccountProduct'), graphql_name='products')
    show_timeline_weekends = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='show_timeline_weekends')
    sign_up_product_kind = sgqlc.types.Field(String, graphql_name='sign_up_product_kind')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    tier = sgqlc.types.Field(String, graphql_name='tier')


class AccountProduct(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('default_workspace_id', 'id', 'kind')
    default_workspace_id = sgqlc.types.Field(ID, graphql_name='default_workspace_id')
    id = sgqlc.types.Field(ID, graphql_name='id')
    kind = sgqlc.types.Field(String, graphql_name='kind')


class AccountRole(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'name', 'role_type')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    role_type = sgqlc.types.Field(String, graphql_name='roleType')


class ActivateUsersError(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('message', 'code', 'user_id')
    message = sgqlc.types.Field(String, graphql_name='message')
    code = sgqlc.types.Field(ActivateUsersErrorCode, graphql_name='code')
    user_id = sgqlc.types.Field(ID, graphql_name='user_id')


class ActivateUsersResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('activated_users', 'errors')
    activated_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='activated_users')
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ActivateUsersError)), graphql_name='errors')


class ActivityLogType(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('account_id', 'created_at', 'data', 'entity', 'event', 'id', 'user_id')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account_id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='created_at')
    data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='data')
    entity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='entity')
    event = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='event')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='user_id')


class AppFeatureType(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'app_id', 'type', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    name = sgqlc.types.Field(String, graphql_name='name')
    app_id = sgqlc.types.Field(ID, graphql_name='app_id')
    type = sgqlc.types.Field(String, graphql_name='type')
    data = sgqlc.types.Field(JSON, graphql_name='data')


class AppInstall(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('app_id', 'app_install_account', 'app_install_user', 'app_version', 'permissions', 'timestamp')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='app_id')
    app_install_account = sgqlc.types.Field(sgqlc.types.non_null('AppInstallAccount'), graphql_name='app_install_account')
    app_install_user = sgqlc.types.Field(sgqlc.types.non_null('AppInstallUser'), graphql_name='app_install_user')
    app_version = sgqlc.types.Field('AppVersion', graphql_name='app_version')
    permissions = sgqlc.types.Field('AppInstallPermissions', graphql_name='permissions')
    timestamp = sgqlc.types.Field(String, graphql_name='timestamp')


class AppInstallAccount(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class AppInstallPermissions(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('approved_scopes', 'required_scopes')
    approved_scopes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='approved_scopes')
    required_scopes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='required_scopes')


class AppInstallUser(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(ID, graphql_name='id')


class AppMonetizationStatus(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('is_supported',)
    is_supported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='is_supported')


class AppSubscription(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('billing_period', 'days_left', 'is_trial', 'max_units', 'plan_id', 'pricing_version', 'renewal_date')
    billing_period = sgqlc.types.Field(String, graphql_name='billing_period')
    days_left = sgqlc.types.Field(Int, graphql_name='days_left')
    is_trial = sgqlc.types.Field(Boolean, graphql_name='is_trial')
    max_units = sgqlc.types.Field(Int, graphql_name='max_units')
    plan_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='plan_id')
    pricing_version = sgqlc.types.Field(Int, graphql_name='pricing_version')
    renewal_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='renewal_date')


class AppSubscriptionDetails(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('account_id', 'plan_id', 'pricing_version_id', 'monthly_price', 'currency', 'period_type', 'renewal_date', 'end_date', 'status', 'discounts', 'days_left')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='account_id')
    plan_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='plan_id')
    pricing_version_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pricing_version_id')
    monthly_price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='monthly_price')
    currency = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currency')
    period_type = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionPeriodType), graphql_name='period_type')
    renewal_date = sgqlc.types.Field(String, graphql_name='renewal_date')
    end_date = sgqlc.types.Field(String, graphql_name='end_date')
    status = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionStatus), graphql_name='status')
    discounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SubscriptionDiscount'))), graphql_name='discounts')
    days_left = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='days_left')


class AppSubscriptionOperationsCounter(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('app_subscription', 'counter_value', 'kind', 'period_key')
    app_subscription = sgqlc.types.Field(AppSubscription, graphql_name='app_subscription')
    counter_value = sgqlc.types.Field(Int, graphql_name='counter_value')
    kind = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kind')
    period_key = sgqlc.types.Field(String, graphql_name='period_key')


class AppSubscriptions(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('subscriptions', 'total_count', 'cursor')
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AppSubscriptionDetails))), graphql_name='subscriptions')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total_count')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')


class AppType(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'created_at', 'updated_at', 'name', 'api_app_id', 'client_id', 'photo_url', 'photo_url_small', 'kind', 'state', 'user_id', 'features')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    name = sgqlc.types.Field(String, graphql_name='name')
    api_app_id = sgqlc.types.Field(ID, graphql_name='api_app_id')
    client_id = sgqlc.types.Field(String, graphql_name='client_id')
    photo_url = sgqlc.types.Field(String, graphql_name='photo_url')
    photo_url_small = sgqlc.types.Field(String, graphql_name='photo_url_small')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    state = sgqlc.types.Field(String, graphql_name='state')
    user_id = sgqlc.types.Field(ID, graphql_name='user_id')
    features = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AppFeatureType)), graphql_name='features', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )


class AppVersion(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('major', 'minor', 'patch', 'text', 'type')
    major = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='major')
    minor = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minor')
    patch = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='patch')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    type = sgqlc.types.Field(String, graphql_name='type')


class AppsMonetizationInfo(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('seats_count',)
    seats_count = sgqlc.types.Field(Int, graphql_name='seats_count')


class Asset(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('created_at', 'file_extension', 'file_size', 'id', 'name', 'original_geometry', 'public_url', 'uploaded_by', 'url', 'url_thumbnail')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    file_extension = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='file_extension')
    file_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='file_size')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    original_geometry = sgqlc.types.Field(String, graphql_name='original_geometry')
    public_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='public_url')
    uploaded_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='uploaded_by')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    url_thumbnail = sgqlc.types.Field(String, graphql_name='url_thumbnail')


class AssignTeamOwnersError(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('message', 'code', 'user_id')
    message = sgqlc.types.Field(String, graphql_name='message')
    code = sgqlc.types.Field(AssignTeamOwnersErrorCode, graphql_name='code')
    user_id = sgqlc.types.Field(ID, graphql_name='user_id')


class AssignTeamOwnersResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('team', 'errors')
    team = sgqlc.types.Field('Team', graphql_name='team')
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AssignTeamOwnersError)), graphql_name='errors')


class BatchExtendTrialPeriod(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('details', 'reason', 'success')
    details = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ExtendTrialPeriod')), graphql_name='details')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class Board(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'views', 'updates', 'activity_logs', 'board_folder_id', 'board_kind', 'columns', 'columns_namespace', 'communication', 'creator', 'description', 'groups', 'item_terminology', 'items_count', 'items_limit', 'items_page', 'name', 'owner', 'owners', 'permissions', 'state', 'subscribers', 'tags', 'team_owners', 'team_subscribers', 'top_group', 'type', 'updated_at', 'url', 'workspace', 'workspace_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    views = sgqlc.types.Field(sgqlc.types.list_of('BoardView'), graphql_name='views', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    updates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Update')), graphql_name='updates', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    activity_logs = sgqlc.types.Field(sgqlc.types.list_of(ActivityLogType), graphql_name='activity_logs', args=sgqlc.types.ArgDict((
        ('column_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='column_ids', default=None)),
        ('from_', sgqlc.types.Arg(ISO8601DateTime, graphql_name='from', default=None)),
        ('group_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='group_ids', default=None)),
        ('item_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='item_ids', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('to', sgqlc.types.Arg(ISO8601DateTime, graphql_name='to', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='user_ids', default=None)),
))
    )
    board_folder_id = sgqlc.types.Field(ID, graphql_name='board_folder_id')
    board_kind = sgqlc.types.Field(sgqlc.types.non_null(BoardKind), graphql_name='board_kind')
    columns = sgqlc.types.Field(sgqlc.types.list_of('Column'), graphql_name='columns', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='ids', default=None)),
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ColumnType)), graphql_name='types', default=None)),
))
    )
    columns_namespace = sgqlc.types.Field(String, graphql_name='columns_namespace')
    communication = sgqlc.types.Field(JSON, graphql_name='communication')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    description = sgqlc.types.Field(String, graphql_name='description')
    groups = sgqlc.types.Field(sgqlc.types.list_of('Group'), graphql_name='groups', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='ids', default=None)),
))
    )
    item_terminology = sgqlc.types.Field(String, graphql_name='item_terminology')
    items_count = sgqlc.types.Field(Int, graphql_name='items_count')
    items_limit = sgqlc.types.Field(Int, graphql_name='items_limit')
    items_page = sgqlc.types.Field(sgqlc.types.non_null('ItemsResponse'), graphql_name='items_page', args=sgqlc.types.ArgDict((
        ('cursor', sgqlc.types.Arg(String, graphql_name='cursor', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=25)),
        ('query_params', sgqlc.types.Arg(ItemsQuery, graphql_name='query_params', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='owner')
    owners = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='owners')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='permissions')
    state = sgqlc.types.Field(sgqlc.types.non_null(State), graphql_name='state')
    subscribers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='subscribers')
    tags = sgqlc.types.Field(sgqlc.types.list_of('Tag'), graphql_name='tags')
    team_owners = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Team')), graphql_name='team_owners', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    team_subscribers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Team')), graphql_name='team_subscribers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    top_group = sgqlc.types.Field(sgqlc.types.non_null('Group'), graphql_name='top_group')
    type = sgqlc.types.Field(BoardObjectType, graphql_name='type')
    updated_at = sgqlc.types.Field(ISO8601DateTime, graphql_name='updated_at')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    workspace = sgqlc.types.Field('Workspace', graphql_name='workspace')
    workspace_id = sgqlc.types.Field(ID, graphql_name='workspace_id')


class BoardDuplication(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('board', 'is_async')
    board = sgqlc.types.Field(sgqlc.types.non_null(Board), graphql_name='board')
    is_async = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='is_async')


class BoardView(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'name', 'type', 'settings_str', 'view_specific_data_str', 'source_view_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(String, graphql_name='type')
    settings_str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='settings_str')
    view_specific_data_str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='view_specific_data_str')
    source_view_id = sgqlc.types.Field(ID, graphql_name='source_view_id')


class ChangeTeamMembershipsResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('failed_users', 'successful_users')
    failed_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='failed_users')
    successful_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='successful_users')


class Column(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('archived', 'description', 'id', 'settings_str', 'title', 'type', 'width')
    archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='archived')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    settings_str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='settings_str')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(ColumnType), graphql_name='type')
    width = sgqlc.types.Field(Int, graphql_name='width')


class Complexity(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('after', 'before', 'query', 'reset_in_x_seconds')
    after = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='after')
    before = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='before')
    query = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='query')
    reset_in_x_seconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='reset_in_x_seconds')


class ConnectProjectResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('request_id', 'success', 'message', 'portfolio_item_id')
    request_id = sgqlc.types.Field(ID, graphql_name='request_id')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')
    portfolio_item_id = sgqlc.types.Field(String, graphql_name='portfolio_item_id')


class Connection(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'account_id', 'user_id', 'provider', 'name', 'method', 'provider_account_identifier', 'state', 'created_at', 'updated_at')
    id = sgqlc.types.Field(Int, graphql_name='id')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    user_id = sgqlc.types.Field(Int, graphql_name='userId')
    provider = sgqlc.types.Field(String, graphql_name='provider')
    name = sgqlc.types.Field(String, graphql_name='name')
    method = sgqlc.types.Field(String, graphql_name='method')
    provider_account_identifier = sgqlc.types.Field(String, graphql_name='providerAccountIdentifier')
    state = sgqlc.types.Field(String, graphql_name='state')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class Country(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('code', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreatePortfolioResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('solution_live_version_id', 'success', 'message')
    solution_live_version_id = sgqlc.types.Field(String, graphql_name='solution_live_version_id')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    message = sgqlc.types.Field(String, graphql_name='message')


class CustomActivity(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'type', 'name', 'icon_id', 'color')
    id = sgqlc.types.Field(ID, graphql_name='id')
    type = sgqlc.types.Field(String, graphql_name='type')
    name = sgqlc.types.Field(String, graphql_name='name')
    icon_id = sgqlc.types.Field(CustomActivityIcon, graphql_name='icon_id')
    color = sgqlc.types.Field(CustomActivityColor, graphql_name='color')


class CustomFieldMetas(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('description', 'editable', 'field_type', 'flagged', 'icon', 'id', 'position', 'title')
    description = sgqlc.types.Field(String, graphql_name='description')
    editable = sgqlc.types.Field(Boolean, graphql_name='editable')
    field_type = sgqlc.types.Field(String, graphql_name='field_type')
    flagged = sgqlc.types.Field(Boolean, graphql_name='flagged')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    id = sgqlc.types.Field(String, graphql_name='id')
    position = sgqlc.types.Field(String, graphql_name='position')
    title = sgqlc.types.Field(String, graphql_name='title')


class CustomFieldValue(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('custom_field_meta_id', 'value')
    custom_field_meta_id = sgqlc.types.Field(String, graphql_name='custom_field_meta_id')
    value = sgqlc.types.Field(String, graphql_name='value')


class DailyAnalytics(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('last_updated', 'by_day', 'by_app', 'by_user')
    last_updated = sgqlc.types.Field(ISO8601DateTime, graphql_name='last_updated')
    by_day = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PlatformApiDailyAnalyticsByDay'))), graphql_name='by_day')
    by_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PlatformApiDailyAnalyticsByApp'))), graphql_name='by_app')
    by_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PlatformApiDailyAnalyticsByUser'))), graphql_name='by_user')


class DailyLimit(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('base', 'total')
    base = sgqlc.types.Field(Int, graphql_name='base')
    total = sgqlc.types.Field(Int, graphql_name='total')


class DeactivateUsersError(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('message', 'code', 'user_id')
    message = sgqlc.types.Field(String, graphql_name='message')
    code = sgqlc.types.Field(DeactivateUsersErrorCode, graphql_name='code')
    user_id = sgqlc.types.Field(ID, graphql_name='user_id')


class DeactivateUsersResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('deactivated_users', 'errors')
    deactivated_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='deactivated_users')
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DeactivateUsersError)), graphql_name='errors')


class DeleteMarketplaceAppDiscount(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('account_slug', 'app_id')
    account_slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account_slug')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='app_id')


class DeleteMarketplaceAppDiscountResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('deleted_discount',)
    deleted_discount = sgqlc.types.Field(sgqlc.types.non_null(DeleteMarketplaceAppDiscount), graphql_name='deleted_discount')


class Document(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('blocks', 'created_at', 'created_by', 'doc_folder_id', 'doc_kind', 'id', 'name', 'object_id', 'relative_url', 'settings', 'url', 'workspace', 'workspace_id')
    blocks = sgqlc.types.Field(sgqlc.types.list_of('DocumentBlock'), graphql_name='blocks', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    created_by = sgqlc.types.Field('User', graphql_name='created_by')
    doc_folder_id = sgqlc.types.Field(ID, graphql_name='doc_folder_id')
    doc_kind = sgqlc.types.Field(sgqlc.types.non_null(BoardKind), graphql_name='doc_kind')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    object_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='object_id')
    relative_url = sgqlc.types.Field(String, graphql_name='relative_url')
    settings = sgqlc.types.Field(JSON, graphql_name='settings')
    url = sgqlc.types.Field(String, graphql_name='url')
    workspace = sgqlc.types.Field('Workspace', graphql_name='workspace')
    workspace_id = sgqlc.types.Field(ID, graphql_name='workspace_id')


class DocumentBlock(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('content', 'created_at', 'created_by', 'doc_id', 'id', 'parent_block_id', 'position', 'type', 'updated_at')
    content = sgqlc.types.Field(JSON, graphql_name='content')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    created_by = sgqlc.types.Field('User', graphql_name='created_by')
    doc_id = sgqlc.types.Field(ID, graphql_name='doc_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    parent_block_id = sgqlc.types.Field(String, graphql_name='parent_block_id')
    position = sgqlc.types.Field(Float, graphql_name='position')
    type = sgqlc.types.Field(String, graphql_name='type')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class DocumentBlockIdOnly(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class DropdownColumnSettings(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('type', 'labels')
    type = sgqlc.types.Field(ManagedColumnTypes, graphql_name='type')
    labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DropdownLabel')), graphql_name='labels')


class DropdownLabel(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'label', 'is_deactivated')
    id = sgqlc.types.Field(Int, graphql_name='id')
    label = sgqlc.types.Field(String, graphql_name='label')
    is_deactivated = sgqlc.types.Field(Boolean, graphql_name='is_deactivated')


class DropdownManagedColumn(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'title', 'description', 'settings_json', 'created_by', 'updated_by', 'revision', 'state', 'created_at', 'updated_at', 'settings')
    id = sgqlc.types.Field(String, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    settings_json = sgqlc.types.Field(JSON, graphql_name='settings_json')
    created_by = sgqlc.types.Field(ID, graphql_name='created_by')
    updated_by = sgqlc.types.Field(ID, graphql_name='updated_by')
    revision = sgqlc.types.Field(Int, graphql_name='revision')
    state = sgqlc.types.Field(ManagedColumnState, graphql_name='state')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    settings = sgqlc.types.Field(DropdownColumnSettings, graphql_name='settings')


class DropdownValueOption(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'label')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')


class ExtendTrialPeriod(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('account_slug', 'reason', 'success')
    account_slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account_slug')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class FileAssetValue(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('asset', 'asset_id', 'created_at', 'creator', 'creator_id', 'is_image', 'name')
    asset = sgqlc.types.Field(sgqlc.types.non_null(Asset), graphql_name='asset')
    asset_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='asset_id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='created_at')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    creator_id = sgqlc.types.Field(ID, graphql_name='creator_id')
    is_image = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='is_image')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class FileDocValue(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('created_at', 'creator', 'creator_id', 'doc', 'file_id', 'object_id', 'url')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='created_at')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    creator_id = sgqlc.types.Field(ID, graphql_name='creator_id')
    doc = sgqlc.types.Field(sgqlc.types.non_null(Document), graphql_name='doc')
    file_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='file_id')
    object_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='object_id')
    url = sgqlc.types.Field(String, graphql_name='url')


class FileLinkValue(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('created_at', 'creator', 'creator_id', 'file_id', 'kind', 'name', 'url')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='created_at')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    creator_id = sgqlc.types.Field(ID, graphql_name='creator_id')
    file_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='file_id')
    kind = sgqlc.types.Field(sgqlc.types.non_null(FileLinkValueKind), graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')


class Folder(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('children', 'color', 'created_at', 'custom_icon', 'font_weight', 'id', 'name', 'owner_id', 'parent', 'sub_folders', 'workspace')
    children = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Board)), graphql_name='children')
    color = sgqlc.types.Field(FolderColor, graphql_name='color')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='created_at')
    custom_icon = sgqlc.types.Field(FolderCustomIcon, graphql_name='custom_icon')
    font_weight = sgqlc.types.Field(FolderFontWeight, graphql_name='font_weight')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner_id = sgqlc.types.Field(ID, graphql_name='owner_id')
    parent = sgqlc.types.Field('Folder', graphql_name='parent')
    sub_folders = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Folder')), graphql_name='sub_folders')
    workspace = sgqlc.types.Field(sgqlc.types.non_null('Workspace'), graphql_name='workspace')


class GrantMarketplaceAppDiscount(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('days_valid', 'discount', 'is_recurring', 'period', 'app_plan_ids', 'app_id')
    days_valid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='days_valid')
    discount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='discount')
    is_recurring = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='is_recurring')
    period = sgqlc.types.Field(DiscountPeriod, graphql_name='period')
    app_plan_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='app_plan_ids')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='app_id')


class GrantMarketplaceAppDiscountResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('granted_discount',)
    granted_discount = sgqlc.types.Field(sgqlc.types.non_null(GrantMarketplaceAppDiscount), graphql_name='granted_discount')


class Group(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('archived', 'color', 'deleted', 'id', 'items_page', 'position', 'title')
    archived = sgqlc.types.Field(Boolean, graphql_name='archived')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    deleted = sgqlc.types.Field(Boolean, graphql_name='deleted')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    items_page = sgqlc.types.Field(sgqlc.types.non_null('ItemsResponse'), graphql_name='items_page', args=sgqlc.types.ArgDict((
        ('cursor', sgqlc.types.Arg(String, graphql_name='cursor', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=25)),
        ('query_params', sgqlc.types.Arg(ItemsQuery, graphql_name='query_params', default=None)),
))
    )
    position = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='position')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class InviteUsersError(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('message', 'code', 'email')
    message = sgqlc.types.Field(String, graphql_name='message')
    code = sgqlc.types.Field(InviteUsersErrorCode, graphql_name='code')
    email = sgqlc.types.Field(ID, graphql_name='email')


class InviteUsersResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('invited_users', 'errors')
    invited_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='invited_users')
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(InviteUsersError)), graphql_name='errors')


class Item(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'updates', 'assets', 'board', 'column_values', 'created_at', 'creator', 'creator_id', 'email', 'group', 'linked_items', 'name', 'parent_item', 'relative_link', 'state', 'subitems', 'subscribers', 'updated_at', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    updates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Update')), graphql_name='updates', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    assets = sgqlc.types.Field(sgqlc.types.list_of(Asset), graphql_name='assets', args=sgqlc.types.ArgDict((
        ('assets_source', sgqlc.types.Arg(AssetsSource, graphql_name='assets_source', default=None)),
        ('column_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='column_ids', default=None)),
))
    )
    board = sgqlc.types.Field(Board, graphql_name='board')
    column_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ColumnValue))), graphql_name='column_values', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ids', default=None)),
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ColumnType)), graphql_name='types', default=None)),
))
    )
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    creator_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='creator_id')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    group = sgqlc.types.Field(Group, graphql_name='group')
    linked_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Item'))), graphql_name='linked_items', args=sgqlc.types.ArgDict((
        ('link_to_item_column_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='link_to_item_column_id', default=None)),
        ('linked_board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='linked_board_id', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_item = sgqlc.types.Field('Item', graphql_name='parent_item')
    relative_link = sgqlc.types.Field(String, graphql_name='relative_link')
    state = sgqlc.types.Field(State, graphql_name='state')
    subitems = sgqlc.types.Field(sgqlc.types.list_of('Item'), graphql_name='subitems')
    subscribers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='subscribers')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class ItemsResponse(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('cursor', 'items')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Item))), graphql_name='items')


class Like(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'creator_id', 'creator', 'reaction_type', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    creator_id = sgqlc.types.Field(String, graphql_name='creator_id')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    reaction_type = sgqlc.types.Field(String, graphql_name='reaction_type')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class ManagedColumn(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'title', 'description', 'settings_json', 'created_by', 'updated_by', 'revision', 'state', 'created_at', 'updated_at', 'settings')
    id = sgqlc.types.Field(String, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    settings_json = sgqlc.types.Field(JSON, graphql_name='settings_json')
    created_by = sgqlc.types.Field(ID, graphql_name='created_by')
    updated_by = sgqlc.types.Field(ID, graphql_name='updated_by')
    revision = sgqlc.types.Field(Int, graphql_name='revision')
    state = sgqlc.types.Field(ManagedColumnState, graphql_name='state')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    settings = sgqlc.types.Field('ColumnSettings', graphql_name='settings')


class MarketplaceAppDiscount(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('account_slug', 'account_id', 'discount', 'is_recurring', 'app_plan_ids', 'period', 'valid_until', 'created_at')
    account_slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account_slug')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='account_id')
    discount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='discount')
    is_recurring = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='is_recurring')
    app_plan_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='app_plan_ids')
    period = sgqlc.types.Field(DiscountPeriod, graphql_name='period')
    valid_until = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='valid_until')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='created_at')


class MirroredItem(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('linked_board', 'linked_board_id', 'linked_item', 'mirrored_value')
    linked_board = sgqlc.types.Field(sgqlc.types.non_null(Board), graphql_name='linked_board')
    linked_board_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linked_board_id')
    linked_item = sgqlc.types.Field(sgqlc.types.non_null(Item), graphql_name='linked_item')
    mirrored_value = sgqlc.types.Field('MirroredValue', graphql_name='mirrored_value')


class Mutation(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('like_update', 'unlike_update', 'delete_update', 'edit_update', 'pin_to_top', 'unpin_from_top', 'create_update', 'create_timeline_item', 'delete_timeline_item', 'create_custom_activity', 'delete_custom_activity', 'create_dropdown_managed_column', 'create_status_managed_column', 'update_dropdown_managed_column', 'update_status_managed_column', 'activate_managed_column', 'deactivate_managed_column', 'delete_managed_column', 'grant_marketplace_app_discount', 'delete_marketplace_app_discount', 'add_file_to_column', 'add_file_to_update', 'add_subscribers_to_board', 'add_teams_to_board', 'add_teams_to_workspace', 'add_users_to_board', 'add_users_to_team', 'add_users_to_workspace', 'archive_board', 'archive_group', 'archive_item', 'batch_extend_trial_period', 'change_column_metadata', 'change_column_title', 'change_column_value', 'change_multiple_column_values', 'change_simple_column_value', 'clear_item_updates', 'complexity', 'create_board', 'create_column', 'create_doc', 'create_doc_block', 'create_folder', 'create_group', 'create_item', 'create_notification', 'create_or_get_tag', 'create_subitem', 'create_webhook', 'create_workspace', 'delete_board', 'delete_column', 'delete_doc_block', 'delete_folder', 'delete_group', 'delete_item', 'delete_subscribers_from_board', 'delete_teams_from_board', 'delete_teams_from_workspace', 'delete_users_from_workspace', 'delete_webhook', 'delete_workspace', 'duplicate_board', 'duplicate_group', 'duplicate_item', 'increase_app_subscription_operations', 'move_item_to_board', 'move_item_to_group', 'remove_mock_app_subscription', 'remove_users_from_team', 'set_mock_app_subscription', 'update_assets_on_item', 'update_board', 'update_doc_block', 'update_folder', 'update_group', 'update_workspace', 'use_template', 'connect_project_to_portfolio', 'create_portfolio', 'create_team', 'activate_users', 'deactivate_users', 'delete_team', 'update_users_role', 'assign_team_owners', 'remove_team_owners', 'update_email_domain', 'update_multiple_users', 'invite_users')
    like_update = sgqlc.types.Field('Update', graphql_name='like_update', args=sgqlc.types.ArgDict((
        ('update_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='update_id', default=None)),
        ('reaction_type', sgqlc.types.Arg(String, graphql_name='reaction_type', default=None)),
))
    )
    unlike_update = sgqlc.types.Field(sgqlc.types.non_null('Update'), graphql_name='unlike_update', args=sgqlc.types.ArgDict((
        ('update_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='update_id', default=None)),
))
    )
    delete_update = sgqlc.types.Field('Update', graphql_name='delete_update', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    edit_update = sgqlc.types.Field(sgqlc.types.non_null('Update'), graphql_name='edit_update', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('body', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='body', default=None)),
))
    )
    pin_to_top = sgqlc.types.Field(sgqlc.types.non_null('Update'), graphql_name='pin_to_top', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
))
    )
    unpin_from_top = sgqlc.types.Field(sgqlc.types.non_null('Update'), graphql_name='unpin_from_top', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
))
    )
    create_update = sgqlc.types.Field('Update', graphql_name='create_update', args=sgqlc.types.ArgDict((
        ('body', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='body', default=None)),
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
        ('parent_id', sgqlc.types.Arg(ID, graphql_name='parent_id', default=None)),
))
    )
    create_timeline_item = sgqlc.types.Field('TimelineItem', graphql_name='create_timeline_item', args=sgqlc.types.ArgDict((
        ('item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='item_id', default=None)),
        ('user_id', sgqlc.types.Arg(Int, graphql_name='user_id', default=None)),
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(ISO8601DateTime), graphql_name='timestamp', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('phone', sgqlc.types.Arg(String, graphql_name='phone', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('time_range', sgqlc.types.Arg(TimelineItemTimeRange, graphql_name='time_range', default=None)),
        ('custom_activity_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='custom_activity_id', default=None)),
))
    )
    delete_timeline_item = sgqlc.types.Field('TimelineItem', graphql_name='delete_timeline_item', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    create_custom_activity = sgqlc.types.Field(CustomActivity, graphql_name='create_custom_activity', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('icon_id', sgqlc.types.Arg(sgqlc.types.non_null(CustomActivityIcon), graphql_name='icon_id', default=None)),
        ('color', sgqlc.types.Arg(sgqlc.types.non_null(CustomActivityColor), graphql_name='color', default=None)),
))
    )
    delete_custom_activity = sgqlc.types.Field(CustomActivity, graphql_name='delete_custom_activity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    create_dropdown_managed_column = sgqlc.types.Field(DropdownManagedColumn, graphql_name='create_dropdown_managed_column', args=sgqlc.types.ArgDict((
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('settings', sgqlc.types.Arg(CreateDropdownColumnSettingsInput, graphql_name='settings', default=None)),
))
    )
    create_status_managed_column = sgqlc.types.Field('StatusManagedColumn', graphql_name='create_status_managed_column', args=sgqlc.types.ArgDict((
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('settings', sgqlc.types.Arg(CreateStatusColumnSettingsInput, graphql_name='settings', default=None)),
))
    )
    update_dropdown_managed_column = sgqlc.types.Field(DropdownManagedColumn, graphql_name='update_dropdown_managed_column', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('settings', sgqlc.types.Arg(UpdateDropdownColumnSettingsInput, graphql_name='settings', default=None)),
        ('revision', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='revision', default=None)),
))
    )
    update_status_managed_column = sgqlc.types.Field('StatusManagedColumn', graphql_name='update_status_managed_column', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('settings', sgqlc.types.Arg(UpdateStatusColumnSettingsInput, graphql_name='settings', default=None)),
        ('revision', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='revision', default=None)),
))
    )
    activate_managed_column = sgqlc.types.Field(ManagedColumn, graphql_name='activate_managed_column', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    deactivate_managed_column = sgqlc.types.Field(ManagedColumn, graphql_name='deactivate_managed_column', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    delete_managed_column = sgqlc.types.Field(ManagedColumn, graphql_name='delete_managed_column', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    grant_marketplace_app_discount = sgqlc.types.Field(sgqlc.types.non_null(GrantMarketplaceAppDiscountResult), graphql_name='grant_marketplace_app_discount', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='app_id', default=None)),
        ('account_slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='account_slug', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(GrantMarketplaceAppDiscountData), graphql_name='data', default=None)),
))
    )
    delete_marketplace_app_discount = sgqlc.types.Field(sgqlc.types.non_null(DeleteMarketplaceAppDiscountResult), graphql_name='delete_marketplace_app_discount', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='app_id', default=None)),
        ('account_slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='account_slug', default=None)),
))
    )
    add_file_to_column = sgqlc.types.Field(Asset, graphql_name='add_file_to_column', args=sgqlc.types.ArgDict((
        ('column_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='column_id', default=None)),
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(File), graphql_name='file', default=None)),
        ('item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='item_id', default=None)),
))
    )
    add_file_to_update = sgqlc.types.Field(Asset, graphql_name='add_file_to_update', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(File), graphql_name='file', default=None)),
        ('update_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='update_id', default=None)),
))
    )
    add_subscribers_to_board = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='add_subscribers_to_board', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('kind', sgqlc.types.Arg(BoardSubscriberKind, graphql_name='kind', default='subscriber')),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
))
    )
    add_teams_to_board = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='add_teams_to_board', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('kind', sgqlc.types.Arg(BoardSubscriberKind, graphql_name='kind', default='subscriber')),
        ('team_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='team_ids', default=None)),
))
    )
    add_teams_to_workspace = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='add_teams_to_workspace', args=sgqlc.types.ArgDict((
        ('kind', sgqlc.types.Arg(WorkspaceSubscriberKind, graphql_name='kind', default='subscriber')),
        ('team_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='team_ids', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspace_id', default=None)),
))
    )
    add_users_to_board = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='add_users_to_board', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('kind', sgqlc.types.Arg(BoardSubscriberKind, graphql_name='kind', default='subscriber')),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
))
    )
    add_users_to_team = sgqlc.types.Field(ChangeTeamMembershipsResult, graphql_name='add_users_to_team', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='team_id', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
))
    )
    add_users_to_workspace = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='add_users_to_workspace', args=sgqlc.types.ArgDict((
        ('kind', sgqlc.types.Arg(WorkspaceSubscriberKind, graphql_name='kind', default='subscriber')),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspace_id', default=None)),
))
    )
    archive_board = sgqlc.types.Field(Board, graphql_name='archive_board', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
))
    )
    archive_group = sgqlc.types.Field(Group, graphql_name='archive_group', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('group_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='group_id', default=None)),
))
    )
    archive_item = sgqlc.types.Field(Item, graphql_name='archive_item', args=sgqlc.types.ArgDict((
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
))
    )
    batch_extend_trial_period = sgqlc.types.Field(BatchExtendTrialPeriod, graphql_name='batch_extend_trial_period', args=sgqlc.types.ArgDict((
        ('account_slugs', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='account_slugs', default=None)),
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='app_id', default=None)),
        ('duration_in_days', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='duration_in_days', default=None)),
        ('plan_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='plan_id', default=None)),
))
    )
    change_column_metadata = sgqlc.types.Field(Column, graphql_name='change_column_metadata', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('column_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='column_id', default=None)),
        ('column_property', sgqlc.types.Arg(ColumnProperty, graphql_name='column_property', default=None)),
        ('value', sgqlc.types.Arg(String, graphql_name='value', default=None)),
))
    )
    change_column_title = sgqlc.types.Field(Column, graphql_name='change_column_title', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('column_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='column_id', default=None)),
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
))
    )
    change_column_value = sgqlc.types.Field(Item, graphql_name='change_column_value', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('column_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='column_id', default=None)),
        ('create_labels_if_missing', sgqlc.types.Arg(Boolean, graphql_name='create_labels_if_missing', default=None)),
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(JSON), graphql_name='value', default=None)),
))
    )
    change_multiple_column_values = sgqlc.types.Field(Item, graphql_name='change_multiple_column_values', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('column_values', sgqlc.types.Arg(sgqlc.types.non_null(JSON), graphql_name='column_values', default=None)),
        ('create_labels_if_missing', sgqlc.types.Arg(Boolean, graphql_name='create_labels_if_missing', default=None)),
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
))
    )
    change_simple_column_value = sgqlc.types.Field(Item, graphql_name='change_simple_column_value', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('column_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='column_id', default=None)),
        ('create_labels_if_missing', sgqlc.types.Arg(Boolean, graphql_name='create_labels_if_missing', default=None)),
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
        ('value', sgqlc.types.Arg(String, graphql_name='value', default=None)),
))
    )
    clear_item_updates = sgqlc.types.Field(Item, graphql_name='clear_item_updates', args=sgqlc.types.ArgDict((
        ('item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='item_id', default=None)),
))
    )
    complexity = sgqlc.types.Field(Complexity, graphql_name='complexity')
    create_board = sgqlc.types.Field(Board, graphql_name='create_board', args=sgqlc.types.ArgDict((
        ('board_kind', sgqlc.types.Arg(sgqlc.types.non_null(BoardKind), graphql_name='board_kind', default=None)),
        ('board_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='board_name', default=None)),
        ('board_owner_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='board_owner_ids', default=None)),
        ('board_owner_team_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='board_owner_team_ids', default=None)),
        ('board_subscriber_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='board_subscriber_ids', default=None)),
        ('board_subscriber_teams_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='board_subscriber_teams_ids', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('empty', sgqlc.types.Arg(Boolean, graphql_name='empty', default=False)),
        ('folder_id', sgqlc.types.Arg(ID, graphql_name='folder_id', default=None)),
        ('template_id', sgqlc.types.Arg(ID, graphql_name='template_id', default=None)),
        ('workspace_id', sgqlc.types.Arg(ID, graphql_name='workspace_id', default=None)),
))
    )
    create_column = sgqlc.types.Field(Column, graphql_name='create_column', args=sgqlc.types.ArgDict((
        ('after_column_id', sgqlc.types.Arg(ID, graphql_name='after_column_id', default=None)),
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('column_type', sgqlc.types.Arg(sgqlc.types.non_null(ColumnType), graphql_name='column_type', default=None)),
        ('defaults', sgqlc.types.Arg(JSON, graphql_name='defaults', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
))
    )
    create_doc = sgqlc.types.Field(Document, graphql_name='create_doc', args=sgqlc.types.ArgDict((
        ('location', sgqlc.types.Arg(sgqlc.types.non_null(CreateDocInput), graphql_name='location', default=None)),
))
    )
    create_doc_block = sgqlc.types.Field(DocumentBlock, graphql_name='create_doc_block', args=sgqlc.types.ArgDict((
        ('after_block_id', sgqlc.types.Arg(String, graphql_name='after_block_id', default=None)),
        ('content', sgqlc.types.Arg(sgqlc.types.non_null(JSON), graphql_name='content', default=None)),
        ('doc_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='doc_id', default=None)),
        ('parent_block_id', sgqlc.types.Arg(String, graphql_name='parent_block_id', default=None)),
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(DocBlockContentType), graphql_name='type', default=None)),
))
    )
    create_folder = sgqlc.types.Field(Folder, graphql_name='create_folder', args=sgqlc.types.ArgDict((
        ('color', sgqlc.types.Arg(FolderColor, graphql_name='color', default=None)),
        ('custom_icon', sgqlc.types.Arg(FolderCustomIcon, graphql_name='custom_icon', default=None)),
        ('font_weight', sgqlc.types.Arg(FolderFontWeight, graphql_name='font_weight', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('parent_folder_id', sgqlc.types.Arg(ID, graphql_name='parent_folder_id', default=None)),
        ('workspace_id', sgqlc.types.Arg(ID, graphql_name='workspace_id', default=None)),
))
    )
    create_group = sgqlc.types.Field(Group, graphql_name='create_group', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('group_color', sgqlc.types.Arg(String, graphql_name='group_color', default=None)),
        ('group_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='group_name', default=None)),
        ('position', sgqlc.types.Arg(String, graphql_name='position', default=None)),
        ('position_relative_method', sgqlc.types.Arg(PositionRelative, graphql_name='position_relative_method', default=None)),
        ('relative_to', sgqlc.types.Arg(String, graphql_name='relative_to', default=None)),
))
    )
    create_item = sgqlc.types.Field(Item, graphql_name='create_item', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('column_values', sgqlc.types.Arg(JSON, graphql_name='column_values', default=None)),
        ('create_labels_if_missing', sgqlc.types.Arg(Boolean, graphql_name='create_labels_if_missing', default=None)),
        ('group_id', sgqlc.types.Arg(String, graphql_name='group_id', default=None)),
        ('item_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='item_name', default=None)),
        ('position_relative_method', sgqlc.types.Arg(PositionRelative, graphql_name='position_relative_method', default=None)),
        ('relative_to', sgqlc.types.Arg(ID, graphql_name='relative_to', default=None)),
))
    )
    create_notification = sgqlc.types.Field('Notification', graphql_name='create_notification', args=sgqlc.types.ArgDict((
        ('target_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='target_id', default=None)),
        ('target_type', sgqlc.types.Arg(sgqlc.types.non_null(NotificationTargetType), graphql_name='target_type', default=None)),
        ('text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='text', default=None)),
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='user_id', default=None)),
))
    )
    create_or_get_tag = sgqlc.types.Field('Tag', graphql_name='create_or_get_tag', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(ID, graphql_name='board_id', default=None)),
        ('tag_name', sgqlc.types.Arg(String, graphql_name='tag_name', default=None)),
))
    )
    create_subitem = sgqlc.types.Field(Item, graphql_name='create_subitem', args=sgqlc.types.ArgDict((
        ('column_values', sgqlc.types.Arg(JSON, graphql_name='column_values', default=None)),
        ('create_labels_if_missing', sgqlc.types.Arg(Boolean, graphql_name='create_labels_if_missing', default=None)),
        ('item_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='item_name', default=None)),
        ('parent_item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='parent_item_id', default=None)),
))
    )
    create_webhook = sgqlc.types.Field('Webhook', graphql_name='create_webhook', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('config', sgqlc.types.Arg(JSON, graphql_name='config', default=None)),
        ('event', sgqlc.types.Arg(sgqlc.types.non_null(WebhookEventType), graphql_name='event', default=None)),
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
))
    )
    create_workspace = sgqlc.types.Field('Workspace', graphql_name='create_workspace', args=sgqlc.types.ArgDict((
        ('account_product_id', sgqlc.types.Arg(ID, graphql_name='account_product_id', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('kind', sgqlc.types.Arg(sgqlc.types.non_null(WorkspaceKind), graphql_name='kind', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    delete_board = sgqlc.types.Field(Board, graphql_name='delete_board', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
))
    )
    delete_column = sgqlc.types.Field(Column, graphql_name='delete_column', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('column_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='column_id', default=None)),
))
    )
    delete_doc_block = sgqlc.types.Field(DocumentBlockIdOnly, graphql_name='delete_doc_block', args=sgqlc.types.ArgDict((
        ('block_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='block_id', default=None)),
))
    )
    delete_folder = sgqlc.types.Field(Folder, graphql_name='delete_folder', args=sgqlc.types.ArgDict((
        ('folder_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='folder_id', default=None)),
))
    )
    delete_group = sgqlc.types.Field(Group, graphql_name='delete_group', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('group_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='group_id', default=None)),
))
    )
    delete_item = sgqlc.types.Field(Item, graphql_name='delete_item', args=sgqlc.types.ArgDict((
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
))
    )
    delete_subscribers_from_board = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='delete_subscribers_from_board', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
))
    )
    delete_teams_from_board = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='delete_teams_from_board', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('team_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='team_ids', default=None)),
))
    )
    delete_teams_from_workspace = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='delete_teams_from_workspace', args=sgqlc.types.ArgDict((
        ('team_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='team_ids', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspace_id', default=None)),
))
    )
    delete_users_from_workspace = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='delete_users_from_workspace', args=sgqlc.types.ArgDict((
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspace_id', default=None)),
))
    )
    delete_webhook = sgqlc.types.Field('Webhook', graphql_name='delete_webhook', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_workspace = sgqlc.types.Field('Workspace', graphql_name='delete_workspace', args=sgqlc.types.ArgDict((
        ('workspace_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='workspace_id', default=None)),
))
    )
    duplicate_board = sgqlc.types.Field(BoardDuplication, graphql_name='duplicate_board', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('board_name', sgqlc.types.Arg(String, graphql_name='board_name', default=None)),
        ('duplicate_type', sgqlc.types.Arg(sgqlc.types.non_null(DuplicateBoardType), graphql_name='duplicate_type', default=None)),
        ('folder_id', sgqlc.types.Arg(ID, graphql_name='folder_id', default=None)),
        ('keep_subscribers', sgqlc.types.Arg(Boolean, graphql_name='keep_subscribers', default=None)),
        ('workspace_id', sgqlc.types.Arg(ID, graphql_name='workspace_id', default=None)),
))
    )
    duplicate_group = sgqlc.types.Field(Group, graphql_name='duplicate_group', args=sgqlc.types.ArgDict((
        ('add_to_top', sgqlc.types.Arg(Boolean, graphql_name='add_to_top', default=None)),
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('group_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='group_id', default=None)),
        ('group_title', sgqlc.types.Arg(String, graphql_name='group_title', default=None)),
))
    )
    duplicate_item = sgqlc.types.Field(Item, graphql_name='duplicate_item', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
        ('with_updates', sgqlc.types.Arg(Boolean, graphql_name='with_updates', default=None)),
))
    )
    increase_app_subscription_operations = sgqlc.types.Field(AppSubscriptionOperationsCounter, graphql_name='increase_app_subscription_operations', args=sgqlc.types.ArgDict((
        ('increment_by', sgqlc.types.Arg(Int, graphql_name='increment_by', default=1)),
        ('kind', sgqlc.types.Arg(String, graphql_name='kind', default='global')),
))
    )
    move_item_to_board = sgqlc.types.Field(Item, graphql_name='move_item_to_board', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('columns_mapping', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ColumnMappingInput)), graphql_name='columns_mapping', default=None)),
        ('group_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='group_id', default=None)),
        ('item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='item_id', default=None)),
        ('subitems_columns_mapping', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ColumnMappingInput)), graphql_name='subitems_columns_mapping', default=None)),
))
    )
    move_item_to_group = sgqlc.types.Field(Item, graphql_name='move_item_to_group', args=sgqlc.types.ArgDict((
        ('group_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='group_id', default=None)),
        ('item_id', sgqlc.types.Arg(ID, graphql_name='item_id', default=None)),
))
    )
    remove_mock_app_subscription = sgqlc.types.Field(AppSubscription, graphql_name='remove_mock_app_subscription', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='app_id', default=None)),
        ('partial_signing_secret', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='partial_signing_secret', default=None)),
))
    )
    remove_users_from_team = sgqlc.types.Field(ChangeTeamMembershipsResult, graphql_name='remove_users_from_team', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='team_id', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
))
    )
    set_mock_app_subscription = sgqlc.types.Field(AppSubscription, graphql_name='set_mock_app_subscription', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='app_id', default=None)),
        ('billing_period', sgqlc.types.Arg(String, graphql_name='billing_period', default=None)),
        ('is_trial', sgqlc.types.Arg(Boolean, graphql_name='is_trial', default=None)),
        ('max_units', sgqlc.types.Arg(Int, graphql_name='max_units', default=None)),
        ('partial_signing_secret', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='partial_signing_secret', default=None)),
        ('plan_id', sgqlc.types.Arg(String, graphql_name='plan_id', default=None)),
        ('pricing_version', sgqlc.types.Arg(Int, graphql_name='pricing_version', default=None)),
        ('renewal_date', sgqlc.types.Arg(Date, graphql_name='renewal_date', default=None)),
))
    )
    update_assets_on_item = sgqlc.types.Field(Item, graphql_name='update_assets_on_item', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('column_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='column_id', default=None)),
        ('files', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FileInput))), graphql_name='files', default=None)),
        ('item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='item_id', default=None)),
))
    )
    update_board = sgqlc.types.Field(JSON, graphql_name='update_board', args=sgqlc.types.ArgDict((
        ('board_attribute', sgqlc.types.Arg(sgqlc.types.non_null(BoardAttributes), graphql_name='board_attribute', default=None)),
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('new_value', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='new_value', default=None)),
))
    )
    update_doc_block = sgqlc.types.Field(DocumentBlock, graphql_name='update_doc_block', args=sgqlc.types.ArgDict((
        ('block_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='block_id', default=None)),
        ('content', sgqlc.types.Arg(sgqlc.types.non_null(JSON), graphql_name='content', default=None)),
))
    )
    update_folder = sgqlc.types.Field(Folder, graphql_name='update_folder', args=sgqlc.types.ArgDict((
        ('color', sgqlc.types.Arg(FolderColor, graphql_name='color', default=None)),
        ('custom_icon', sgqlc.types.Arg(FolderCustomIcon, graphql_name='custom_icon', default=None)),
        ('folder_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='folder_id', default=None)),
        ('font_weight', sgqlc.types.Arg(FolderFontWeight, graphql_name='font_weight', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('parent_folder_id', sgqlc.types.Arg(ID, graphql_name='parent_folder_id', default=None)),
))
    )
    update_group = sgqlc.types.Field(Group, graphql_name='update_group', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('group_attribute', sgqlc.types.Arg(sgqlc.types.non_null(GroupAttributes), graphql_name='group_attribute', default=None)),
        ('group_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='group_id', default=None)),
        ('new_value', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='new_value', default=None)),
))
    )
    update_workspace = sgqlc.types.Field('Workspace', graphql_name='update_workspace', args=sgqlc.types.ArgDict((
        ('attributes', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkspaceAttributesInput), graphql_name='attributes', default=None)),
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    use_template = sgqlc.types.Field('Template', graphql_name='use_template', args=sgqlc.types.ArgDict((
        ('board_kind', sgqlc.types.Arg(BoardKind, graphql_name='board_kind', default=None)),
        ('board_owner_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='board_owner_ids', default=None)),
        ('board_owner_team_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='board_owner_team_ids', default=None)),
        ('board_subscriber_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='board_subscriber_ids', default=None)),
        ('board_subscriber_teams_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='board_subscriber_teams_ids', default=None)),
        ('callback_url_on_complete', sgqlc.types.Arg(String, graphql_name='callback_url_on_complete', default=None)),
        ('destination_folder_id', sgqlc.types.Arg(Int, graphql_name='destination_folder_id', default=None)),
        ('destination_folder_name', sgqlc.types.Arg(String, graphql_name='destination_folder_name', default=None)),
        ('destination_name', sgqlc.types.Arg(String, graphql_name='destination_name', default=None)),
        ('destination_workspace_id', sgqlc.types.Arg(Int, graphql_name='destination_workspace_id', default=None)),
        ('skip_target_folder_creation', sgqlc.types.Arg(Boolean, graphql_name='skip_target_folder_creation', default=None)),
        ('solution_extra_options', sgqlc.types.Arg(JSON, graphql_name='solution_extra_options', default=None)),
        ('template_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='template_id', default=None)),
))
    )
    connect_project_to_portfolio = sgqlc.types.Field(ConnectProjectResult, graphql_name='connect_project_to_portfolio', args=sgqlc.types.ArgDict((
        ('project_board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectBoardId', default=None)),
        ('portfolio_board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='portfolioBoardId', default=None)),
))
    )
    create_portfolio = sgqlc.types.Field(CreatePortfolioResult, graphql_name='create_portfolio', args=sgqlc.types.ArgDict((
        ('board_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='boardName', default=None)),
        ('board_privacy', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='boardPrivacy', default=None)),
        ('destination_workspace_id', sgqlc.types.Arg(Int, graphql_name='destinationWorkspaceId', default=None)),
))
    )
    create_team = sgqlc.types.Field('Team', graphql_name='create_team', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTeamAttributesInput), graphql_name='input', default=None)),
        ('options', sgqlc.types.Arg(CreateTeamOptionsInput, graphql_name='options', default=None)),
))
    )
    activate_users = sgqlc.types.Field(ActivateUsersResult, graphql_name='activate_users', args=sgqlc.types.ArgDict((
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
))
    )
    deactivate_users = sgqlc.types.Field(DeactivateUsersResult, graphql_name='deactivate_users', args=sgqlc.types.ArgDict((
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
))
    )
    delete_team = sgqlc.types.Field('Team', graphql_name='delete_team', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='team_id', default=None)),
))
    )
    update_users_role = sgqlc.types.Field('UpdateUsersRoleResult', graphql_name='update_users_role', args=sgqlc.types.ArgDict((
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
        ('new_role', sgqlc.types.Arg(BaseRoleName, graphql_name='new_role', default=None)),
        ('role_id', sgqlc.types.Arg(ID, graphql_name='role_id', default=None)),
))
    )
    assign_team_owners = sgqlc.types.Field(AssignTeamOwnersResult, graphql_name='assign_team_owners', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='team_id', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
))
    )
    remove_team_owners = sgqlc.types.Field('RemoveTeamOwnersResult', graphql_name='remove_team_owners', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='team_id', default=None)),
        ('user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='user_ids', default=None)),
))
    )
    update_email_domain = sgqlc.types.Field('UpdateEmailDomainResult', graphql_name='update_email_domain', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEmailDomainAttributesInput), graphql_name='input', default=None)),
))
    )
    update_multiple_users = sgqlc.types.Field('UpdateUserAttributesResult', graphql_name='update_multiple_users', args=sgqlc.types.ArgDict((
        ('user_updates', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserUpdateInput))), graphql_name='user_updates', default=None)),
        ('bypass_confirmation_for_claimed_domains', sgqlc.types.Arg(Boolean, graphql_name='bypass_confirmation_for_claimed_domains', default=None)),
))
    )
    invite_users = sgqlc.types.Field(InviteUsersResult, graphql_name='invite_users', args=sgqlc.types.ArgDict((
        ('emails', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='emails', default=None)),
        ('user_role', sgqlc.types.Arg(UserRole, graphql_name='user_role', default=None)),
        ('product', sgqlc.types.Arg(Product, graphql_name='product', default=None)),
))
    )


class Notification(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'text', 'read')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    text = sgqlc.types.Field(String, graphql_name='text')
    read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='read')


class OutOfOffice(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('active', 'disable_notifications', 'end_date', 'start_date', 'type')
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    disable_notifications = sgqlc.types.Field(Boolean, graphql_name='disable_notifications')
    end_date = sgqlc.types.Field(Date, graphql_name='end_date')
    start_date = sgqlc.types.Field(Date, graphql_name='start_date')
    type = sgqlc.types.Field(String, graphql_name='type')


class PeopleEntity(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'kind')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    kind = sgqlc.types.Field(Kind, graphql_name='kind')


class Plan(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('max_users', 'period', 'tier', 'version')
    max_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='max_users')
    period = sgqlc.types.Field(String, graphql_name='period')
    tier = sgqlc.types.Field(String, graphql_name='tier')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')


class PlatformApi(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('daily_limit', 'daily_analytics')
    daily_limit = sgqlc.types.Field(DailyLimit, graphql_name='daily_limit')
    daily_analytics = sgqlc.types.Field(DailyAnalytics, graphql_name='daily_analytics')


class PlatformApiDailyAnalyticsByApp(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('app', 'usage', 'api_app_id')
    app = sgqlc.types.Field(AppType, graphql_name='app')
    usage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usage')
    api_app_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='api_app_id')


class PlatformApiDailyAnalyticsByDay(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('day', 'usage')
    day = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='day')
    usage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usage')


class PlatformApiDailyAnalyticsByUser(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('user', 'usage')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    usage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usage')


class Query(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('get_live_workflows', 'get_workflow_variable_schemas', 'get_workflow_block_next_mapping_schemas', 'connections', 'user_connections', 'account_connections', 'connection', 'connection_board_ids', 'updates', 'custom_activity', 'timeline_item', 'timeline', 'managed_column', 'marketplace_app_discounts', 'app_subscriptions', 'app', 'account', 'app_installs', 'app_subscription', 'app_subscription_operations', 'apps_monetization_info', 'apps_monetization_status', 'assets', 'boards', 'complexity', 'docs', 'folders', 'items', 'items_page_by_column_values', 'me', 'next_items_page', 'tags', 'teams', 'users', 'webhooks', 'workspaces', 'version', 'versions', 'platform_api', 'account_roles')
    get_live_workflows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Workflow')), graphql_name='get_live_workflows', args=sgqlc.types.ArgDict((
        ('host_instance_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='hostInstanceId', default=None)),
        ('host_type', sgqlc.types.Arg(sgqlc.types.non_null(HostType), graphql_name='hostType', default=None)),
        ('pagination', sgqlc.types.Arg(PaginationInput, graphql_name='pagination', default=None)),
))
    )
    get_workflow_variable_schemas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkflowVariableSchema'))), graphql_name='get_workflow_variable_schemas')
    get_workflow_block_next_mapping_schemas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkflowBlockNextMappingSchema'))), graphql_name='get_workflow_block_next_mapping_schemas')
    connections = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Connection)), graphql_name='connections', args=sgqlc.types.ArgDict((
        ('with_automations', sgqlc.types.Arg(Boolean, graphql_name='withAutomations', default=None)),
        ('connection_state', sgqlc.types.Arg(String, graphql_name='connectionState', default=None)),
        ('with_state_validation', sgqlc.types.Arg(Boolean, graphql_name='withStateValidation', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('order', sgqlc.types.Arg(String, graphql_name='order', default=None)),
        ('with_partial_scopes', sgqlc.types.Arg(Boolean, graphql_name='withPartialScopes', default=None)),
        ('pagination', sgqlc.types.Arg(PaginationInput, graphql_name='pagination', default=None)),
))
    )
    user_connections = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Connection)), graphql_name='user_connections', args=sgqlc.types.ArgDict((
        ('with_automations', sgqlc.types.Arg(Boolean, graphql_name='withAutomations', default=None)),
        ('with_state_validation', sgqlc.types.Arg(Boolean, graphql_name='withStateValidation', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('order', sgqlc.types.Arg(String, graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(PaginationInput, graphql_name='pagination', default=None)),
))
    )
    account_connections = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Connection)), graphql_name='account_connections', args=sgqlc.types.ArgDict((
        ('with_automations', sgqlc.types.Arg(Boolean, graphql_name='withAutomations', default=None)),
        ('with_state_validation', sgqlc.types.Arg(Boolean, graphql_name='withStateValidation', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('order', sgqlc.types.Arg(String, graphql_name='order', default=None)),
        ('pagination', sgqlc.types.Arg(PaginationInput, graphql_name='pagination', default=None)),
))
    )
    connection = sgqlc.types.Field(Connection, graphql_name='connection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    connection_board_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='connection_board_ids', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='connectionId', default=None)),
))
    )
    updates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Update')), graphql_name='updates', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    custom_activity = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CustomActivity)), graphql_name='custom_activity', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ids', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('icon_id', sgqlc.types.Arg(CustomActivityIcon, graphql_name='icon_id', default=None)),
        ('color', sgqlc.types.Arg(CustomActivityColor, graphql_name='color', default=None)),
))
    )
    timeline_item = sgqlc.types.Field('TimelineItem', graphql_name='timeline_item', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    timeline = sgqlc.types.Field('TimelineResponse', graphql_name='timeline', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    managed_column = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ManagedColumn)), graphql_name='managed_column', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id', default=None)),
        ('state', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ManagedColumnState)), graphql_name='state', default=None)),
))
    )
    marketplace_app_discounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MarketplaceAppDiscount))), graphql_name='marketplace_app_discounts', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='app_id', default=None)),
))
    )
    app_subscriptions = sgqlc.types.Field(sgqlc.types.non_null(AppSubscriptions), graphql_name='app_subscriptions', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='app_id', default=None)),
        ('status', sgqlc.types.Arg(SubscriptionStatus, graphql_name='status', default=None)),
        ('account_id', sgqlc.types.Arg(Int, graphql_name='account_id', default=None)),
        ('cursor', sgqlc.types.Arg(String, graphql_name='cursor', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    app = sgqlc.types.Field(AppType, graphql_name='app', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    account = sgqlc.types.Field(Account, graphql_name='account')
    app_installs = sgqlc.types.Field(sgqlc.types.list_of(AppInstall), graphql_name='app_installs', args=sgqlc.types.ArgDict((
        ('account_id', sgqlc.types.Arg(ID, graphql_name='account_id', default=None)),
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='app_id', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    app_subscription = sgqlc.types.Field(sgqlc.types.list_of(AppSubscription), graphql_name='app_subscription')
    app_subscription_operations = sgqlc.types.Field(AppSubscriptionOperationsCounter, graphql_name='app_subscription_operations', args=sgqlc.types.ArgDict((
        ('kind', sgqlc.types.Arg(String, graphql_name='kind', default='global')),
))
    )
    apps_monetization_info = sgqlc.types.Field(AppsMonetizationInfo, graphql_name='apps_monetization_info')
    apps_monetization_status = sgqlc.types.Field(AppMonetizationStatus, graphql_name='apps_monetization_status')
    assets = sgqlc.types.Field(sgqlc.types.list_of(Asset), graphql_name='assets', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    boards = sgqlc.types.Field(sgqlc.types.list_of(Board), graphql_name='boards', args=sgqlc.types.ArgDict((
        ('board_kind', sgqlc.types.Arg(BoardKind, graphql_name='board_kind', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
        ('latest', sgqlc.types.Arg(Boolean, graphql_name='latest', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('order_by', sgqlc.types.Arg(BoardsOrderBy, graphql_name='order_by', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('state', sgqlc.types.Arg(State, graphql_name='state', default='active')),
        ('workspace_ids', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='workspace_ids', default=None)),
))
    )
    complexity = sgqlc.types.Field(Complexity, graphql_name='complexity')
    docs = sgqlc.types.Field(sgqlc.types.list_of(Document), graphql_name='docs', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('object_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='object_ids', default=None)),
        ('order_by', sgqlc.types.Arg(DocsOrderBy, graphql_name='order_by', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('workspace_ids', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='workspace_ids', default=None)),
))
    )
    folders = sgqlc.types.Field(sgqlc.types.list_of(Folder), graphql_name='folders', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('workspace_ids', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='workspace_ids', default=None)),
))
    )
    items = sgqlc.types.Field(sgqlc.types.list_of(Item), graphql_name='items', args=sgqlc.types.ArgDict((
        ('exclude_nonactive', sgqlc.types.Arg(Boolean, graphql_name='exclude_nonactive', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('newest_first', sgqlc.types.Arg(Boolean, graphql_name='newest_first', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    items_page_by_column_values = sgqlc.types.Field(sgqlc.types.non_null(ItemsResponse), graphql_name='items_page_by_column_values', args=sgqlc.types.ArgDict((
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
        ('columns', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ItemsPageByColumnValuesQuery)), graphql_name='columns', default=None)),
        ('cursor', sgqlc.types.Arg(String, graphql_name='cursor', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=25)),
))
    )
    me = sgqlc.types.Field('User', graphql_name='me')
    next_items_page = sgqlc.types.Field(sgqlc.types.non_null(ItemsResponse), graphql_name='next_items_page', args=sgqlc.types.ArgDict((
        ('cursor', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='cursor', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=25)),
))
    )
    tags = sgqlc.types.Field(sgqlc.types.list_of('Tag'), graphql_name='tags', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    users = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('emails', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='emails', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
        ('kind', sgqlc.types.Arg(UserKind, graphql_name='kind', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('newest_first', sgqlc.types.Arg(Boolean, graphql_name='newest_first', default=None)),
        ('non_active', sgqlc.types.Arg(Boolean, graphql_name='non_active', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
))
    )
    webhooks = sgqlc.types.Field(sgqlc.types.list_of('Webhook'), graphql_name='webhooks', args=sgqlc.types.ArgDict((
        ('app_webhooks_only', sgqlc.types.Arg(Boolean, graphql_name='app_webhooks_only', default=None)),
        ('board_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='board_id', default=None)),
))
    )
    workspaces = sgqlc.types.Field(sgqlc.types.list_of('Workspace'), graphql_name='workspaces', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
        ('kind', sgqlc.types.Arg(WorkspaceKind, graphql_name='kind', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('order_by', sgqlc.types.Arg(WorkspacesOrderBy, graphql_name='order_by', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
        ('state', sgqlc.types.Arg(State, graphql_name='state', default='active')),
))
    )
    version = sgqlc.types.Field(sgqlc.types.non_null('Version'), graphql_name='version')
    versions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Version')), graphql_name='versions')
    platform_api = sgqlc.types.Field(PlatformApi, graphql_name='platform_api')
    account_roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AccountRole)), graphql_name='account_roles')


class RemoveTeamOwnersError(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('message', 'code', 'user_id')
    message = sgqlc.types.Field(String, graphql_name='message')
    code = sgqlc.types.Field(RemoveTeamOwnersErrorCode, graphql_name='code')
    user_id = sgqlc.types.Field(ID, graphql_name='user_id')


class RemoveTeamOwnersResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('team', 'errors')
    team = sgqlc.types.Field('Team', graphql_name='team')
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RemoveTeamOwnersError)), graphql_name='errors')


class Reply(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'body', 'kind', 'creator_id', 'edited_at', 'creator', 'likes', 'pinned_to_top', 'viewers', 'created_at', 'updated_at', 'text_body')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    kind = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kind')
    creator_id = sgqlc.types.Field(String, graphql_name='creator_id')
    edited_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='edited_at')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    likes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Like))), graphql_name='likes')
    pinned_to_top = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdatePin'))), graphql_name='pinned_to_top')
    viewers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Watcher'))), graphql_name='viewers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    text_body = sgqlc.types.Field(String, graphql_name='text_body')


class StatusColumnSettings(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('type', 'labels')
    type = sgqlc.types.Field(ManagedColumnTypes, graphql_name='type')
    labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StatusLabel')), graphql_name='labels')


class StatusLabel(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'label', 'color', 'index', 'description', 'is_deactivated', 'is_done')
    id = sgqlc.types.Field(Int, graphql_name='id')
    label = sgqlc.types.Field(String, graphql_name='label')
    color = sgqlc.types.Field(StatusColumnColors, graphql_name='color')
    index = sgqlc.types.Field(Int, graphql_name='index')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_deactivated = sgqlc.types.Field(Boolean, graphql_name='is_deactivated')
    is_done = sgqlc.types.Field(Boolean, graphql_name='is_done')


class StatusLabelStyle(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('border', 'color')
    border = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='border')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')


class StatusManagedColumn(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'title', 'description', 'settings_json', 'created_by', 'updated_by', 'revision', 'state', 'created_at', 'updated_at', 'settings')
    id = sgqlc.types.Field(String, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    settings_json = sgqlc.types.Field(JSON, graphql_name='settings_json')
    created_by = sgqlc.types.Field(ID, graphql_name='created_by')
    updated_by = sgqlc.types.Field(ID, graphql_name='updated_by')
    revision = sgqlc.types.Field(Int, graphql_name='revision')
    state = sgqlc.types.Field(ManagedColumnState, graphql_name='state')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    settings = sgqlc.types.Field(StatusColumnSettings, graphql_name='settings')


class SubscriptionDiscount(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('value', 'discount_model_type', 'discount_type')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')
    discount_model_type = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionDiscountModelType), graphql_name='discount_model_type')
    discount_type = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionDiscountType), graphql_name='discount_type')


class Tag(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('color', 'id', 'name')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Team(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'owners', 'picture_url', 'users', 'name', 'is_guest')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    owners = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='owners', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    picture_url = sgqlc.types.Field(String, graphql_name='picture_url')
    users = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('emails', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='emails', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
        ('kind', sgqlc.types.Arg(UserKind, graphql_name='kind', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('newest_first', sgqlc.types.Arg(Boolean, graphql_name='newest_first', default=None)),
        ('non_active', sgqlc.types.Arg(Boolean, graphql_name='non_active', default=None)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_guest = sgqlc.types.Field(Boolean, graphql_name='is_guest')


class Template(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('process_id',)
    process_id = sgqlc.types.Field(String, graphql_name='process_id')


class TimeTrackingHistoryItem(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('created_at', 'ended_at', 'ended_user_id', 'id', 'manually_entered_end_date', 'manually_entered_end_time', 'manually_entered_start_date', 'manually_entered_start_time', 'started_at', 'started_user_id', 'status', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='created_at')
    ended_at = sgqlc.types.Field(Date, graphql_name='ended_at')
    ended_user_id = sgqlc.types.Field(ID, graphql_name='ended_user_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    manually_entered_end_date = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='manually_entered_end_date')
    manually_entered_end_time = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='manually_entered_end_time')
    manually_entered_start_date = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='manually_entered_start_date')
    manually_entered_start_time = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='manually_entered_start_time')
    started_at = sgqlc.types.Field(Date, graphql_name='started_at')
    started_user_id = sgqlc.types.Field(ID, graphql_name='started_user_id')
    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class TimelineItem(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'type', 'item', 'board', 'user', 'title', 'custom_activity_id', 'content', 'created_at')
    id = sgqlc.types.Field(ID, graphql_name='id')
    type = sgqlc.types.Field(String, graphql_name='type')
    item = sgqlc.types.Field(Item, graphql_name='item')
    board = sgqlc.types.Field(Board, graphql_name='board')
    user = sgqlc.types.Field('User', graphql_name='user')
    title = sgqlc.types.Field(String, graphql_name='title')
    custom_activity_id = sgqlc.types.Field(String, graphql_name='custom_activity_id')
    content = sgqlc.types.Field(String, graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='created_at')


class TimelineItemsPage(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('timeline_items', 'cursor')
    timeline_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TimelineItem))), graphql_name='timeline_items')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')


class TimelineResponse(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('timeline_items_page',)
    timeline_items_page = sgqlc.types.Field(sgqlc.types.non_null(TimelineItemsPage), graphql_name='timeline_items_page', args=sgqlc.types.ArgDict((
        ('cursor', sgqlc.types.Arg(String, graphql_name='cursor', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
))
    )


class Update(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'body', 'creator_id', 'edited_at', 'creator', 'likes', 'pinned_to_top', 'viewers', 'created_at', 'updated_at', 'item_id', 'item', 'replies', 'assets', 'text_body')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    creator_id = sgqlc.types.Field(String, graphql_name='creator_id')
    edited_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='edited_at')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    likes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Like))), graphql_name='likes')
    pinned_to_top = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdatePin'))), graphql_name='pinned_to_top')
    viewers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Watcher'))), graphql_name='viewers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    item_id = sgqlc.types.Field(String, graphql_name='item_id')
    item = sgqlc.types.Field(Item, graphql_name='item')
    replies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Reply)), graphql_name='replies')
    assets = sgqlc.types.Field(sgqlc.types.list_of(Asset), graphql_name='assets')
    text_body = sgqlc.types.Field(String, graphql_name='text_body')


class UpdateEmailDomainError(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('message', 'code', 'user_id')
    message = sgqlc.types.Field(String, graphql_name='message')
    code = sgqlc.types.Field(UpdateEmailDomainErrorCode, graphql_name='code')
    user_id = sgqlc.types.Field(ID, graphql_name='user_id')


class UpdateEmailDomainResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('updated_users', 'errors')
    updated_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='updated_users')
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UpdateEmailDomainError)), graphql_name='errors')


class UpdatePin(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('item_id',)
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='item_id')


class UpdateUserAttributesError(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('message', 'code', 'user_id')
    message = sgqlc.types.Field(String, graphql_name='message')
    code = sgqlc.types.Field(UpdateUserAttributesErrorCode, graphql_name='code')
    user_id = sgqlc.types.Field(ID, graphql_name='user_id')


class UpdateUserAttributesResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('updated_users', 'errors')
    updated_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='updated_users')
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UpdateUserAttributesError)), graphql_name='errors')


class UpdateUsersRoleError(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('message', 'code', 'user_id')
    message = sgqlc.types.Field(String, graphql_name='message')
    code = sgqlc.types.Field(UpdateUsersRoleErrorCode, graphql_name='code')
    user_id = sgqlc.types.Field(ID, graphql_name='user_id')


class UpdateUsersRoleResult(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('updated_users', 'errors')
    updated_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='updated_users')
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UpdateUsersRoleError)), graphql_name='errors')


class User(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'account', 'account_products', 'birthday', 'country_code', 'created_at', 'current_language', 'custom_field_metas', 'custom_field_values', 'email', 'enabled', 'encrypt_api_token', 'is_admin', 'is_guest', 'is_pending', 'is_verified', 'is_view_only', 'join_date', 'last_activity', 'location', 'mobile_phone', 'name', 'out_of_office', 'phone', 'photo_original', 'photo_small', 'photo_thumb', 'photo_thumb_small', 'photo_tiny', 'sign_up_product_kind', 'teams', 'time_zone_identifier', 'title', 'url', 'utc_hours_diff', 'greeting')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    account_products = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AccountProduct)), graphql_name='account_products')
    birthday = sgqlc.types.Field(Date, graphql_name='birthday')
    country_code = sgqlc.types.Field(String, graphql_name='country_code')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    current_language = sgqlc.types.Field(String, graphql_name='current_language')
    custom_field_metas = sgqlc.types.Field(sgqlc.types.list_of(CustomFieldMetas), graphql_name='custom_field_metas')
    custom_field_values = sgqlc.types.Field(sgqlc.types.list_of(CustomFieldValue), graphql_name='custom_field_values')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    encrypt_api_token = sgqlc.types.Field(String, graphql_name='encrypt_api_token')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='is_admin')
    is_guest = sgqlc.types.Field(Boolean, graphql_name='is_guest')
    is_pending = sgqlc.types.Field(Boolean, graphql_name='is_pending')
    is_verified = sgqlc.types.Field(Boolean, graphql_name='is_verified')
    is_view_only = sgqlc.types.Field(Boolean, graphql_name='is_view_only')
    join_date = sgqlc.types.Field(Date, graphql_name='join_date')
    last_activity = sgqlc.types.Field(Date, graphql_name='last_activity')
    location = sgqlc.types.Field(String, graphql_name='location')
    mobile_phone = sgqlc.types.Field(String, graphql_name='mobile_phone')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    out_of_office = sgqlc.types.Field(OutOfOffice, graphql_name='out_of_office')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    photo_original = sgqlc.types.Field(String, graphql_name='photo_original')
    photo_small = sgqlc.types.Field(String, graphql_name='photo_small')
    photo_thumb = sgqlc.types.Field(String, graphql_name='photo_thumb')
    photo_thumb_small = sgqlc.types.Field(String, graphql_name='photo_thumb_small')
    photo_tiny = sgqlc.types.Field(String, graphql_name='photo_tiny')
    sign_up_product_kind = sgqlc.types.Field(String, graphql_name='sign_up_product_kind')
    teams = sgqlc.types.Field(sgqlc.types.list_of(Team), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    time_zone_identifier = sgqlc.types.Field(String, graphql_name='time_zone_identifier')
    title = sgqlc.types.Field(String, graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    utc_hours_diff = sgqlc.types.Field(Int, graphql_name='utc_hours_diff')
    greeting = sgqlc.types.Field(String, graphql_name='greeting')


class Version(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('display_name', 'kind', 'value')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='display_name')
    kind = sgqlc.types.Field(sgqlc.types.non_null(VersionKind), graphql_name='kind')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class Watcher(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('user_id', 'medium', 'user')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='user_id')
    medium = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='medium')
    user = sgqlc.types.Field(User, graphql_name='user')


class Webhook(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('board_id', 'config', 'event', 'id')
    board_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='board_id')
    config = sgqlc.types.Field(String, graphql_name='config')
    event = sgqlc.types.Field(sgqlc.types.non_null(WebhookEventType), graphql_name='event')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class Workflow(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('id', 'title', 'description', 'workflow_blocks', 'workflow_variables', 'workflow_host_data', 'host_type', 'host_instance_id', 'notice_message', 'creator_app_feature_reference_id', 'creator_app_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    workflow_blocks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('WorkflowBlock')), graphql_name='workflowBlocks')
    workflow_variables = sgqlc.types.Field(JSON, graphql_name='workflowVariables')
    workflow_host_data = sgqlc.types.Field('WorkflowHostData', graphql_name='workflowHostData')
    host_type = sgqlc.types.Field(HostType, graphql_name='hostType')
    host_instance_id = sgqlc.types.Field(Int, graphql_name='hostInstanceId')
    notice_message = sgqlc.types.Field(String, graphql_name='noticeMessage')
    creator_app_feature_reference_id = sgqlc.types.Field(Int, graphql_name='creatorAppFeatureReferenceId')
    creator_app_id = sgqlc.types.Field(Int, graphql_name='creatorAppId')


class WorkflowBlock(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('workflow_node_id', 'block_reference_id', 'title', 'input_fields', 'credentials_source_config', 'next_workflow_blocks_config', 'kind')
    workflow_node_id = sgqlc.types.Field(Int, graphql_name='workflowNodeId')
    block_reference_id = sgqlc.types.Field(Int, graphql_name='blockReferenceId')
    title = sgqlc.types.Field(String, graphql_name='title')
    input_fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('WorkflowBlockInputField')), graphql_name='inputFields')
    credentials_source_config = sgqlc.types.Field(JSON, graphql_name='credentialsSourceConfig')
    next_workflow_blocks_config = sgqlc.types.Field(JSON, graphql_name='nextWorkflowBlocksConfig')
    kind = sgqlc.types.Field(WorkflowBlockKind, graphql_name='kind')


class WorkflowBlockInputField(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('field_key', 'workflow_variable_key')
    field_key = sgqlc.types.Field(String, graphql_name='fieldKey')
    workflow_variable_key = sgqlc.types.Field(Int, graphql_name='workflowVariableKey')


class WorkflowBlockNextMappingSchema(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('kind', 'schema')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    schema = sgqlc.types.Field(JSON, graphql_name='schema')


class WorkflowHostData(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('type', 'id')
    type = sgqlc.types.Field(HostType, graphql_name='type')
    id = sgqlc.types.Field(Int, graphql_name='id')


class WorkflowVariableSchema(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('kind', 'schema')
    kind = sgqlc.types.Field(WorkflowVariableSourceKind, graphql_name='kind')
    schema = sgqlc.types.Field(JSON, graphql_name='schema')


class Workspace(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('account_product', 'created_at', 'description', 'id', 'is_default_workspace', 'kind', 'name', 'owners_subscribers', 'settings', 'state', 'team_owners_subscribers', 'teams_subscribers', 'users_subscribers')
    account_product = sgqlc.types.Field(AccountProduct, graphql_name='account_product')
    created_at = sgqlc.types.Field(Date, graphql_name='created_at')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    is_default_workspace = sgqlc.types.Field(Boolean, graphql_name='is_default_workspace')
    kind = sgqlc.types.Field(WorkspaceKind, graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owners_subscribers = sgqlc.types.Field(sgqlc.types.list_of(User), graphql_name='owners_subscribers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    settings = sgqlc.types.Field('WorkspaceSettings', graphql_name='settings')
    state = sgqlc.types.Field(State, graphql_name='state')
    team_owners_subscribers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Team)), graphql_name='team_owners_subscribers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    teams_subscribers = sgqlc.types.Field(sgqlc.types.list_of(Team), graphql_name='teams_subscribers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )
    users_subscribers = sgqlc.types.Field(sgqlc.types.list_of(User), graphql_name='users_subscribers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=25)),
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=1)),
))
    )


class WorkspaceIcon(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('color', 'image')
    color = sgqlc.types.Field(String, graphql_name='color')
    image = sgqlc.types.Field(String, graphql_name='image')


class WorkspaceSettings(sgqlc.types.Type):
    __schema__ = monday_schema
    __field_names__ = ('icon',)
    icon = sgqlc.types.Field(WorkspaceIcon, graphql_name='icon')


class BoardRelationValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('display_value', 'linked_item_ids', 'linked_items', 'updated_at')
    display_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='display_value')
    linked_item_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='linked_item_ids')
    linked_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Item))), graphql_name='linked_items')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class ButtonValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('color', 'label')
    color = sgqlc.types.Field(String, graphql_name='color')
    label = sgqlc.types.Field(String, graphql_name='label')


class CheckboxValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('checked', 'updated_at')
    checked = sgqlc.types.Field(Boolean, graphql_name='checked')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class ColorPickerValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('color', 'updated_at')
    color = sgqlc.types.Field(String, graphql_name='color')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class CountryValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('country', 'updated_at')
    country = sgqlc.types.Field(Country, graphql_name='country')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class CreationLogValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('created_at', 'creator', 'creator_id')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='created_at')
    creator = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='creator')
    creator_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='creator_id')


class DateValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('date', 'icon', 'time', 'updated_at')
    date = sgqlc.types.Field(String, graphql_name='date')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    time = sgqlc.types.Field(String, graphql_name='time')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class DependencyValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('display_value', 'linked_item_ids', 'linked_items', 'updated_at')
    display_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='display_value')
    linked_item_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='linked_item_ids')
    linked_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Item))), graphql_name='linked_items')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class DirectDocValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('file',)
    file = sgqlc.types.Field('DirectDocValue', graphql_name='file')


class DocValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('file',)
    file = sgqlc.types.Field(FileDocValue, graphql_name='file')


class DropdownValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('values',)
    values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DropdownValueOption))), graphql_name='values')


class EmailValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('email', 'label', 'updated_at')
    email = sgqlc.types.Field(String, graphql_name='email')
    label = sgqlc.types.Field(String, graphql_name='label')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class FileValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('files',)
    files = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FileValueItem'))), graphql_name='files')


class FormulaValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('display_value',)
    display_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='display_value')


class GroupValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('group', 'group_id')
    group = sgqlc.types.Field(Group, graphql_name='group')
    group_id = sgqlc.types.Field(ID, graphql_name='group_id')


class HourValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('hour', 'minute', 'updated_at')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class IntegrationValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('entity_id', 'issue_api_url', 'issue_id')
    entity_id = sgqlc.types.Field(ID, graphql_name='entity_id')
    issue_api_url = sgqlc.types.Field(ID, graphql_name='issue_api_url')
    issue_id = sgqlc.types.Field(String, graphql_name='issue_id')


class ItemIdValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('item_id',)
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='item_id')


class LastUpdatedValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('updated_at', 'updater', 'updater_id')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    updater = sgqlc.types.Field(User, graphql_name='updater')
    updater_id = sgqlc.types.Field(ID, graphql_name='updater_id')


class LinkValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('updated_at', 'url', 'url_text')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    url = sgqlc.types.Field(String, graphql_name='url')
    url_text = sgqlc.types.Field(String, graphql_name='url_text')


class LocationValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('address', 'city', 'city_short', 'country', 'country_short', 'lat', 'lng', 'place_id', 'street', 'street_number', 'street_number_short', 'street_short', 'updated_at')
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(String, graphql_name='city')
    city_short = sgqlc.types.Field(String, graphql_name='city_short')
    country = sgqlc.types.Field(String, graphql_name='country')
    country_short = sgqlc.types.Field(String, graphql_name='country_short')
    lat = sgqlc.types.Field(Float, graphql_name='lat')
    lng = sgqlc.types.Field(Float, graphql_name='lng')
    place_id = sgqlc.types.Field(String, graphql_name='place_id')
    street = sgqlc.types.Field(String, graphql_name='street')
    street_number = sgqlc.types.Field(String, graphql_name='street_number')
    street_number_short = sgqlc.types.Field(String, graphql_name='street_number_short')
    street_short = sgqlc.types.Field(String, graphql_name='street_short')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class LongTextValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('updated_at',)
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class MirrorValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('display_value', 'mirrored_items')
    display_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='display_value')
    mirrored_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MirroredItem))), graphql_name='mirrored_items')


class NumbersValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('direction', 'number', 'symbol')
    direction = sgqlc.types.Field(NumberValueUnitDirection, graphql_name='direction')
    number = sgqlc.types.Field(Float, graphql_name='number')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')


class PeopleValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('persons_and_teams', 'updated_at')
    persons_and_teams = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PeopleEntity)), graphql_name='persons_and_teams')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class PersonValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('person_id', 'updated_at')
    person_id = sgqlc.types.Field(ID, graphql_name='person_id')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class PhoneValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('country_short_name', 'phone', 'updated_at')
    country_short_name = sgqlc.types.Field(String, graphql_name='country_short_name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class ProgressValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ()


class RatingValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('rating', 'updated_at')
    rating = sgqlc.types.Field(Int, graphql_name='rating')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class StatusValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('index', 'is_done', 'label', 'label_style', 'update_id', 'updated_at')
    index = sgqlc.types.Field(Int, graphql_name='index')
    is_done = sgqlc.types.Field(Boolean, graphql_name='is_done')
    label = sgqlc.types.Field(String, graphql_name='label')
    label_style = sgqlc.types.Field(StatusLabelStyle, graphql_name='label_style')
    update_id = sgqlc.types.Field(ID, graphql_name='update_id')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class SubtasksValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('display_value', 'subitems', 'subitems_ids')
    display_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='display_value')
    subitems = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Item))), graphql_name='subitems')
    subitems_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='subitems_ids')


class TagsValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('tag_ids', 'tags')
    tag_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='tag_ids')
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Tag))), graphql_name='tags')


class TeamValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('team_id', 'updated_at')
    team_id = sgqlc.types.Field(Int, graphql_name='team_id')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class TextValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ()


class TimeTrackingValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('duration', 'history', 'running', 'started_at', 'updated_at')
    duration = sgqlc.types.Field(Int, graphql_name='duration')
    history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TimeTrackingHistoryItem))), graphql_name='history')
    running = sgqlc.types.Field(Boolean, graphql_name='running')
    started_at = sgqlc.types.Field(Date, graphql_name='started_at')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')


class TimelineValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('from_', 'to', 'updated_at', 'visualization_type')
    from_ = sgqlc.types.Field(Date, graphql_name='from')
    to = sgqlc.types.Field(Date, graphql_name='to')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    visualization_type = sgqlc.types.Field(String, graphql_name='visualization_type')


class UnsupportedValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ()


class VoteValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('updated_at', 'vote_count', 'voter_ids', 'voters')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')
    vote_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='vote_count')
    voter_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='voter_ids')
    voters = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(User))), graphql_name='voters')


class WeekValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('end_date', 'start_date')
    end_date = sgqlc.types.Field(Date, graphql_name='end_date')
    start_date = sgqlc.types.Field(Date, graphql_name='start_date')


class WorldClockValue(sgqlc.types.Type, ColumnValue):
    __schema__ = monday_schema
    __field_names__ = ('timezone', 'updated_at')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    updated_at = sgqlc.types.Field(Date, graphql_name='updated_at')



########################################################################
# Unions
########################################################################
class ColumnSettings(sgqlc.types.Union):
    __schema__ = monday_schema
    __types__ = (StatusColumnSettings, DropdownColumnSettings)


class FileValueItem(sgqlc.types.Union):
    __schema__ = monday_schema
    __types__ = (FileAssetValue, FileDocValue, FileLinkValue)


class MirroredValue(sgqlc.types.Union):
    __schema__ = monday_schema
    __types__ = (Board, BoardRelationValue, ButtonValue, CheckboxValue, ColorPickerValue, CountryValue, CreationLogValue, DateValue, DependencyValue, DirectDocValue, DocValue, DropdownValue, EmailValue, FileValue, FormulaValue, Group, GroupValue, HourValue, IntegrationValue, ItemIdValue, LastUpdatedValue, LinkValue, LocationValue, LongTextValue, MirrorValue, NumbersValue, PeopleValue, PersonValue, PhoneValue, ProgressValue, RatingValue, StatusValue, SubtasksValue, TagsValue, TeamValue, TextValue, TimeTrackingValue, TimelineValue, UnsupportedValue, VoteValue, WeekValue, WorldClockValue)



########################################################################
# Schema Entry Points
########################################################################
monday_schema.query_type = Query
monday_schema.mutation_type = Mutation
monday_schema.subscription_type = None

