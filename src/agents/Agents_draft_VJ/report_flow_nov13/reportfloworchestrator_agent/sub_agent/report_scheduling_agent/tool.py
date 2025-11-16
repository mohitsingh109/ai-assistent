def schedule_new_report(
    template_id: str,
    schedule_type: str,
    delivery_time: str,
    recipient_emails: list[str],
    timezone: str = 'UTC',
    day_of_week: str = None,
    day_of_month: int = None
) -> dict:
    """
    Schedules a new report for delivery based on a saved template.

    Args:
        template_id: (Required) The unique ID of the report template to schedule.
        schedule_type: (Required) The frequency of the report run. Must be 'ONE_TIME', 'DAILY', 'WEEKLY', or 'MONTHLY'.
        delivery_time: (Required) The time of day the report should be delivered, in 'HH:MM' 24-hour format (e.g., '08:30').
        recipient_emails: (Required) A list of email addresses that should receive the report file.
        timezone: (Optional) The IANA time zone for the delivery time (e.g., 'America/New_York'). Defaults to 'UTC'.
        day_of_week: (Optional) Required if schedule_type is 'WEEKLY'. Must be a three-letter weekday (e.g., 'MON', 'TUE').
        day_of_month: (Optional) Required if schedule_type is 'MONTHLY'. Must be an integer (1-28) or -1 for the last day of the month.

    Returns:
        dict: Status, the new schedule ID, and a confirmation message.
    """
    # Tool logic implementation goes here
    pass

def update_report_schedule(
    schedule_id: str,
    schedule_type: str = None,
    delivery_time: str = None,
    recipient_emails: list[str] = None,
    timezone: str = None,
    day_of_week: str = None,
    day_of_month: int = None,
    is_enabled: bool = None
) -> dict:
    """
    Modifies an existing scheduled report's properties, delivery time, recurrence, or status.

    Args:
        schedule_id: (Required) The unique ID of the scheduled report to update.
        schedule_type: (Optional) New frequency: 'ONE_TIME', 'DAILY', 'WEEKLY', or 'MONTHLY'.
        delivery_time: (Optional) New delivery time in 'HH:MM' 24-hour format.
        recipient_emails: (Optional) New list of email addresses to receive the report.
        timezone: (Optional) New IANA time zone.
        day_of_week: (Optional) New three-letter weekday for 'WEEKLY' schedules.
        day_of_month: (Optional) New day of the month for 'MONTHLY' schedules (1-28 or -1).
        is_enabled: (Optional) Set to True to enable or False to disable the schedule.

    Returns:
        dict: Status and the updated schedule details.
    """
    # Tool logic implementation goes here
    pass


def list_report_schedules(
    template_id: str = None,
    status: str = 'ALL',
    search_term: str = None
) -> dict:
    """
    Retrieves a list of scheduled reports based on filtering criteria.

    Args:
        template_id: (Optional) Filter schedules tied to a specific report template ID.
        status: (Optional) Filter by status. Must be 'ENABLED', 'DISABLED', or 'ALL'. Defaults to 'ALL'.
        search_term: (Optional) Keyword to search within schedule names or recipient emails.

    Returns:
        dict: Status and a list of matching report schedule objects.
    """
    # Tool logic implementation goes here
    pass

def delete_report_schedule(
    schedule_id: str
) -> dict:
    """
    Permanently deletes a scheduled report job by its ID.

    Args:
        schedule_id: (Required) The unique ID of the scheduled report to delete.

    Returns:
        dict: Status and a confirmation message.
    """
    # Tool logic implementation goes here
    pass