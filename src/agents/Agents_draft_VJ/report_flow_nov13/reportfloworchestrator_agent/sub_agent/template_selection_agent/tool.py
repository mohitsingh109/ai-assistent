from typing import List, Dict, Any
import uuid
import json
import os

# Define the file path for the external template data source
#TEMPLATE_DATA_FILE = "adk-learning-Vijaya-independent/report_flow_nov13/reportfloworchestrator_agent/sub_agent/template_selection_agent/template_list.json"
TEMPLATE_DATA_FILE= [
    {
        "id": "388a6a7b-1405-4fe2-b352-eb0fc6bde269",
        "name": "Demographics: Basic",
        "description": "Basic demographic breakdown for all participants.",
        "category": "demographics",
        "config": {
            "required_fields": ["participant_id"],
            "optional_fields": ["participant_country"],
            "filters": {}
        }
    },
    {
        "id": "f4d65171-986f-4ed5-b1a5-a0e1a4adf7db",
        "name": "Demographics: By Country",
        "description": "Demographics filtered by participant country.",
        "category": "demographics",
        "config": {
            "required_fields": ["participant_id", "participant_country"],
            "optional_fields": ["company_unit_id"],
            "filters": {
                "participant_country": "US"
            }
        }
    },
    {
        "id": "321f163b-e14e-46df-b0b4-593211f13c72",
        "name": "Asset: Overview (Legacy)",
        "description": "Overview of assets based on type and status.",
        "category": "asset",
        "config": {
            "required_fields": ["asset_type", "asset_status"],
            "optional_fields": [],
            "filters": {}
        }
    },
    {
        "id": "a9d3c5f2-901b-4ef8-a476-8e92f2b4e7a1",
        "name": "Compliance: Incomplete Checklist UK",
        "description": "Report on UK participants with incomplete mandatory checklists.",
        "category": "compliance",
        "config": {
            "required_fields": ["participant_id", "incomplete_checklist_count", "company_unit_id"],
            "optional_fields": [],
            "filters": {
                "participant_country": "UK",
                "incomplete_checklist_count": ">0"
            }
        }
    },
    {
        "id": "d0e1b2c3-4f5a-6b7c-8d9e-0f1a2b3c4d5e",
        "name": "Grants: Summary UK Participants",
        "description": "Summary of total granted quantity for participants in the UK.",
        "category": "grants",
        "config": {
            "required_fields": ["participant_id", "granted_quantity"],
            "optional_fields": ["grant_id", "grant_date"],
            "filters": {
                "participant_country": "UK"
            }
        }
    },
    {
        "id": "1e2f3g4h-5i6j-7k8l-9m0n-1o2p3q4r5s6t",
        "name": "Vesting: Next Tranche Forecast (All Regions)",
        "description": "Forecast of upcoming vesting events and tranche sizes across all regions.",
        "category": "vesting_schedule",
        "config": {
            "required_fields": ["vesting_date", "next_vesting_tranche_size"],
            "optional_fields": ["participant_id", "grant_id"],
            "filters": {}
        }
    },
    {
        "id": "9876z5y4-3x2w-1v0u-9t8s-7r6q5p4o3n2m",
        "name": "Plans: Launch Date History",
        "description": "A list of equity/retirement plans and their official launch dates.",
        "category": "plans",
        "config": {
            "required_fields": ["plan_name", "plan_launch_date"],
            "optional_fields": [],
            "filters": {}
        }
    },

    {
        "id": "5f6e7d8c-2b1a-4c3d-9e0f-1a2b3c4d5e6f",
        "name": "Vesting: Vested Quantity UK",
        "description": "Report on the quantity of shares/units already vested for UK participants.",
        "category": "vesting_schedule",
        "config": {
            "required_fields": ["participant_id", "vested_quantity"],
            "optional_fields": ["grant_id", "vesting_date"],
            "filters": {
                "participant_country": "UK"
            }
        }
    },
    {
        "id": "4b2a6c1e-8d5f-7g9h-0i3j-2k5l8m1n4o7p",
        "name": "Grants: Detail by Company Unit UK",
        "description": "Detailed grant report, breaking down granted quantity by internal company unit for UK.",
        "category": "grants",
        "config": {
            "required_fields": ["company_unit_id", "granted_quantity", "grant_id"],
            "optional_fields": ["grant_date", "participant_id"],
            "filters": {
                "participant_country": "UK"
            }
        }
    },
    {
        "id": "c1f9e8d7-6a5b-4c3d-2e1f-0g9h8i7j6k5l",
        "name": "Vesting: Next Tranche Forecast UK",
        "description": "Forecast of the next vesting event details and tranche sizes, filtered for the UK.",
        "category": "vesting_schedule",
        "config": {
            "required_fields": ["participant_id", "vesting_date", "next_vesting_tranche_size"],
            "optional_fields": ["grant_id"],
            "filters": {
                "participant_country": "UK"
            }
        }
    }
]





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




# --- Template Discovery Agent Tools ---

# def list_templates() -> List[Dict[str, Any]]:
#     """
#     Returns the current list of templates by reading the external JSON file.
#     This is the core function for retrieving all template data.
#     """
#     a=_load_templates()
#     print(f"this is the template list {a}")
#     return _load_templates()

def list_templates() -> List[Dict[str, Any]]:
    """Return all available templates"""
    return TEMPLATE_DATA_FILE.copy()

def fetch_all_templates() -> List[Dict[str, Any]]:
    """
    Retrieves the complete list of all available report templates from the system.

    This is the core tool for the Template Discovery Agent to begin searching,
    filtering, and comparing existing templates against a user's request.
    """
    print("--- Tool: fetch_all_templates called ---")
    return list_templates()

def describe_template_tool(template_id: str) -> Dict[str, Any]:
    """
    Fetches the detailed configuration for a specific report template, including all required input fields.
    """
    templates = list_templates()
    for t in templates:
        if t.get("id") == template_id:
            return t
    return {"error": "template not found"}


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



