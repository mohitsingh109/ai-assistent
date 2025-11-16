from google.adk.agents import LlmAgent, Agent
from src.agents.template_creation.tools import list_template, list_available_data_points

template_creation_agent = LlmAgent(
    name="template_creation",
    model="gemini-2.0-flash",
    description="Create or expand templates.",
    instruction= """
    You will help users to create new template.
    if user want to expend <Template name> first list existing template
    the describe that template  then propose additional data points using 
    the list_available_data_point tool, confirm the user choice
    ask for template name & description then call the create_template tool.
    
    Return the new template id and a clean summary
    """,
    tools=[list_template, list_available_data_points]
)