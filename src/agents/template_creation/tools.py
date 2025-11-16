from typing import List, Dict, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from google.adk.tools import ToolContext


# from model.report import Templates


# (Post Gemini)
# async def list_template(
#         tool_context: ToolContext
# ) -> List[Dict]:
#     """
#     Returns existing template ....
#
#     Args:
#         tool_context: (injected) Provide access to DB session and state
#     Returns:
#         A list of template with id, name and description
#     """
#
#     session: AsyncSession = tool_context.state.get("db_session")
#
#     # session will help us to query the DB (open search) to fetch all the template
#     templates = None
#     # we'll replace the below code once we integrate the open search
#     if not templates:
#         templates = TEMPLATE
#
#     return templates

# After Gemini
async def list_template(
        tool_context: ToolContext
) -> List[Dict]:
    """
    Retrieves a complete list of all available **Templates** from the database.

    Each template in the returned list is a detailed object containing its unique 'id',
    display 'name', a short 'description', a 'category' (e.g., 'demographics'), and
    a 'config' dictionary specifying the 'required_fields' and 'filters' needed to run the analysis.

    This tool is used to show the user which templates are available for selection based on the user query.

    Args:
        tool_context: (injected) Provide access to DB session and state
    """

    session: AsyncSession = tool_context.state.get("db_session")

    # session will help us to query the DB (open search) to fetch all the template
    templates = None
    # we'll replace the below code once we integrate the open search
    if not templates:
        templates = TEMPLATE

    return templates


# We'll may modify this to access some argument and then filter out the data points
async def list_available_data_points() -> Dict:
    """
     Return available data points that can be used to build template
    """
    return DATA_POINTS


async def create_template(
        base_template_id: Optional[str],
        name: str,
        description: Optional[str],
        selected_fields: List[str],
        filters: Optional[List[Dict]],
        tool_context: ToolContext
) -> Dict:
    """

    Args:
        base_template_id: Existing template id tp expand from or None
        name: New template name
        description: Optional template description
        selected_fields: List of fields identified from available data points to include in the template
        filters: Filter (e.g [ { "field:": "participant_country", "value": "US", "operator": "eq"} ])
        tool_context: Provided db session
    Returns:
        Dict with new template id and basic metadata
    """

    session: AsyncSession = tool_context.state.get("db_session")

    """
    Code we'll create later the object of Template
    new_template = None
    session.save(new_template)
    """





# we'll move it to open search
TEMPLATE = [
    {
        "id": "388a6a7b-1405-4fe2-b352-eb0fc6bde269",
        "name": "Demographics: Basic",
        "description": "Basic demographic breakdown for all participants.",
        "category": "demographics",
        "config": {
            "selected_fields": ["participant_id", "participant_country"],
            "filters": {}
        }
    },
    {
        "id": "f4d65171-986f-4ed5-b1a5-a0e1a4adf7db",
        "name": "Demographics: By Country",
        "description": "Demographics filtered by participant country.",
        "category": "demographics",
        "config": {
            "selected_fields": ["participant_id", "participant_country", "company_unit_id"],
            "filters": [
                {
                    "field:": "participant_country",
                    "value": "US",
                    "operator": "eq"
                }
            ]
        }
    },
    {
        "id": "321f163b-e14e-46df-b0b4-593211f13c72",
        "name": "Asset: Overview (Legacy)",
        "description": "Overview of assets based on type and status.",
        "category": "asset",
        "config": {
            "selected_fields": ["asset_type", "asset_status"],
            "filters": {}
        }
    },
    {
        "id": "a9d3c5f2-901b-4ef8-a476-8e92f2b4e7a1",
        "name": "Compliance: Incomplete Checklist UK",
        "description": "Report on UK participants with incomplete mandatory checklists.",
        "category": "compliance",
        "config": {
            "selected_fields": ["participant_id", "incomplete_checklist_count", "company_unit_id"],
            "filters": [
                {
                    "field:": "participant_country",
                    "value": "UK",
                    "operator": "eq"
                },
                {
                    "field:": "incomplete_checklist_count",
                    "value": 0,
                    "operator": "gt"
                }
            ]
        }
    },
    {
        "id": "d0e1b2c3-4f5a-6b7c-8d9e-0f1a2b3c4d5e",
        "name": "Grants: Summary UK Participants",
        "description": "Summary of total granted quantity for participants in the UK.",
        "category": "grants",
        "config": {
            "selected_fields": ["participant_id", "granted_quantity", "grant_id", "grant_date"],
            "filters": [
                {
                    "field:": "participant_country",
                    "value": "UK",
                    "operator": "eq"
                },
            ]
        }
    },
    {
        "id": "1e2f3g4h-5i6j-7k8l-9m0n-1o2p3q4r5s6t",
        "name": "Vesting: Next Tranche Forecast (All Regions)",
        "description": "Forecast of upcoming vesting events and tranche sizes across all regions.",
        "category": "vesting_schedule",
        "config": {
            "required_fields": ["vesting_date", "next_vesting_tranche_size", "participant_id", "grant_id"],
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
            "filters": {}
        }
    },

    {
        "id": "5f6e7d8c-2b1a-4c3d-9e0f-1a2b3c4d5e6f",
        "name": "Vesting: Vested Quantity UK",
        "description": "Report on the quantity of shares/units already vested for UK participants.",
        "category": "vesting_schedule",
        "config": {
            "required_fields": ["participant_id", "vested_quantity", "grant_id", "vesting_date"],
            "filters": [
                {
                    "field:": "participant_country",
                    "value": "UK",
                    "operator": "eq"
                },
            ]
        }
    },
    {
        "id": "4b2a6c1e-8d5f-7g9h-0i3j-2k5l8m1n4o7p",
        "name": "Grants: Detail by Company Unit UK",
        "description": "Detailed grant report, breaking down granted quantity by internal company unit for UK.",
        "category": "grants",
        "config": {
            "required_fields": ["company_unit_id", "granted_quantity", "grant_id", "grant_date", "participant_id"],
            "filters": [
                {
                    "field:": "participant_country",
                    "value": "UK",
                    "operator": "eq"
                },
            ]
        }
    },
    {
        "id": "c1f9e8d7-6a5b-4c3d-2e1f-0g9h8i7j6k5l",
        "name": "Vesting: Next Tranche Forecast UK",
        "description": "Forecast of the next vesting event details and tranche sizes, filtered for the UK.",
        "category": "vesting_schedule",
        "config": {
            "required_fields": ["participant_id", "vesting_date", "next_vesting_tranche_size", "grant_id"],
            "filters": [
                {
                    "field:": "participant_country",
                    "value": "UK",
                    "operator": "eq"
                },
            ]
        }
    }
]

# we'll move it to open search
DATA_POINTS = {
    "Participants": [
        {
            "field_name": "participant_id",
            "description": "Unique identifier for each user or participant.",
            "tags": ["demographics", "id", "personal"]
        },
        {
            "field_name": "participant_country",
            "description": "The country where the participant is located (e.g., US, UK, DE).",
            "tags": ["demographics", "location", "geo", "filter"]
        },
        {
            "field_name": "incomplete_checklist_count",
            "description": "Count of incomplete mandatory action items or checklists for a participant.",
            "tags": ["compliance", "checklist"]
        },
        {
            "field_name": "company_unit_id",
            "description": "ID representing the organizational unit or company branch.",
            "tags": ["organization", "filter"]
        }
    ],
    "Plans": [
        {
            "field_name": "plan_name",
            "description": "The name of the equity or retirement plan (e.g., ESPP, RSU Plan 2023).",
            "tags": ["equity", "type", "filter"]
        },
        {
            "field_name": "plan_launch_date",
            "description": "The date the plan was officially launched.",
            "tags": ["date", "metadata"]
        }
    ],
    "Grants": [
        {
            "field_name": "grant_id",
            "description": "Unique identifier for a specific award or grant.",
            "tags": ["equity", "id", "award"]
        },
        {
            "field_name": "grant_date",
            "description": "The date the grant was awarded to the participant.",
            "tags": ["date", "award"]
        },
        {
            "field_name": "granted_quantity",
            "description": "The number of shares or units originally granted.",
            "tags": ["quantity", "metric"]
        }
    ],
    "Vesting Schedule": [
        {
            "field_name": "vesting_date",
            "description": "The specific date when a tranche of the grant vests.",
            "tags": ["date", "schedule", "filter"]
        },
        {
            "field_name": "vested_quantity",
            "description": "The number of shares or units that have vested to date.",
            "tags": ["quantity", "metric"]
        },
        {
            "field_name": "next_vesting_tranche_size",
            "description": "The number of units scheduled to vest next.",
            "tags": ["quantity", "future"]
        }
    ],
    "Assets (Legacy)": [
        {
            "field_name": "asset_type",
            "description": "The type or category of the asset (e.g., equipment, vehicle, property).",
            "tags": ["asset", "inventory", "category"]
        },
        {
            "field_name": "asset_status",
            "description": "The current operational status of the asset (e.g., active, maintenance, retired).",
            "tags": ["asset", "status", "filter"]
        }
    ]
}
