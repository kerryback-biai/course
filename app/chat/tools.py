"""Claude tool definitions for the data assistant."""
from app.database.duckdb_manager import SYSTEM_NAMES

QUERY_DATABASE_TOOL = {
    "name": "query_database",
    "description": (
        "Execute a read-only SQL query against a specific enterprise system. "
        "Each system has its own tables with its own naming conventions and ID schemes. "
        "You CANNOT join across systems in a single query. "
        "To combine data from multiple systems, query each separately and use code_execution to merge with Python. "
        "Returns columns and rows as JSON. Maximum 500 rows returned."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "sql": {
                "type": "string",
                "description": "A SELECT SQL query to execute against the specified system's tables.",
            },
            "system": {
                "type": "string",
                "enum": SYSTEM_NAMES,
                "description": "The enterprise system to query.",
            },
        },
        "required": ["sql", "system"],
    },
}

CODE_EXECUTION_TOOL = {
    "type": "code_execution_20250522",
    "name": "code_execution",
}


def get_tools() -> list[dict]:
    return [QUERY_DATABASE_TOOL, CODE_EXECUTION_TOOL]
