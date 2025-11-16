from typing import List, Dict, Any
import uuid
import json
import os

# Define the file path for the external template data source
TEMPLATE_DATA_FILE = "/adk-learning-Vijaya-independent/report_flow/report_orchestrator_agent/sub_agent/Data/template_list.json"
MDB_SCHEMA_FILE = "/adk-learning-Vijaya-independent/report_flow/report_orchestrator_agent/sub_agent/Data/master_database_schema.json"

# --- Internal File I/O Functions (Simulating Database Interaction) ---

def _load_templates() -> List[Dict[str, Any]]:
    """Loads the template list from the external JSON file."""
    try:
        with open(TEMPLATE_DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {TEMPLATE_DATA_FILE} not found. Returning empty list.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {TEMPLATE_DATA_FILE}. Returning empty list.")
        return []

def _save_templates(templates: List[Dict[str, Any]]):
    """Saves the current template list to the external JSON file."""
    try:
        with open(TEMPLATE_DATA_FILE, 'w') as f:
            json.dump(templates, f, indent=4)
    except IOError as e:
        print(f"Error saving templates to {TEMPLATE_DATA_FILE}: {e}")

def _load_mdb_schema() -> Dict[str, List[Dict[str, Any]]]:
    """
    Loads the Master Data Base schema from the external JSON file,
    which is now structured by categories.
    """
    try:
        with open(MDB_SCHEMA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {MDB_SCHEMA_FILE} not found. Returning empty schema.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {MDB_SCHEMA_FILE}.")
        return {}






def search_master_data_points(query: str) -> List[str]:
    """
    Searches the Master Data Base (MDB) schema for fields relevant to the given query.

    This tool is crucial for the Template Discovery Agent when a new report is needed,
    to identify available data fields for inclusion. The search is case-insensitive
    and checks field names, descriptions, and tags across all defined categories.

    Args:
        query: The user's search term (e.g., 'UK', 'vesting date', 'plan name').

    Returns:
        A list of unique 'field_name' strings that match the query.
        Example: ['participant_country', 'vesting_date']
    """
    print(f"--- Tool: search_master_data_points called with query: '{query}' ---")
    schema = _load_mdb_schema()
    query_lower = query.lower()
    matching_fields = set()

    # Iterate over the categories (dictionary values)
    # schema is now a dict: {"Participants": [field1, field2], "Plans": [...]}
    for category_name, fields in schema.items():
        # Iterate over the list of fields within each category
        for field in fields:
            # Check field name
            if query_lower in field.get("field_name", "").lower():
                matching_fields.add(field["field_name"])
                continue

            # Check description
            if query_lower in field.get("description", "").lower():
                matching_fields.add(field["field_name"])
                continue

            # Check tags
            for tag in field.get("tags", []):
                if query_lower in tag.lower():
                    matching_fields.add(field["field_name"])
                    break

    return sorted(list(matching_fields))


def search_master_data_points(query: str) -> List[str]:
    """
    Searches the Master Data Base (MDB) schema for fields relevant to the given query.

    The tool is used during the template creation process to help the user identify
    and select the specific data fields they want to include in their new report.

    Args:
        query: The user's search term (e.g., 'UK', 'vesting date', 'plan name').

    Returns:
        A list of unique 'field_name' strings that match the query.
    """
    # (Implementation would mirror the one in the selection agent's toolset)
    pass

def save_new_template(
    name: str,
    description: str,
    required_fields: List[str],
    default_filters: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Saves a fully configured new report template to the system.

    This is the final step in the template creation process. The agent must
    gather all necessary parameters from the user dialogue before calling this tool.

    Args:
        name: The user-defined name for the new template (e.g., "Q4 Equity Summary").
        description: A brief summary of the template's purpose.
        required_fields: A list of the specific MDB field names included in the report.
        default_filters: A JSON object defining any default filters (e.g., {"country": "US", "status": "Active"}).

    Returns:
        A dictionary containing the new template's ID and name upon successful save,
        or an error message if the save fails.
        Example: {"id": "1a2b3c4d-5e6f-7g8h-9i0j-k1l2m3n4o5p6", "name": "Q4 Equity Summary"}
    """
    # (Implementation would generate a UUID, save to the JSON file, and return the metadata)
    pass



