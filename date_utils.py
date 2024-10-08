from datetime import datetime, timedelta
import pytz


def get_current_ist_time():
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist)


def get_formatted_date(date):
    return date.strftime("%Y-%m-%d")


def get_formatted_time(date):
    return date.strftime("%I:%M %p IST")


def get_week_dates(start_date=None):
    ist = pytz.timezone('Asia/Kolkata')
    if start_date:
        # If start_date is already a date object, convert it to datetime
        if isinstance(start_date, datetime):
            start_datetime = start_date
        else:  # It's a date object
            start_datetime = datetime.combine(start_date, datetime.min.time())
        start_datetime = ist.localize(start_datetime)
    else:
        start_datetime = get_current_ist_time()

    week_dates = []
    for i in range(7):
        date = start_datetime + timedelta(days=i)
        week_dates.append(get_formatted_date(date))
    return week_dates


def get_optimal_posting_times():
    return ["9:30 AM IST", "1:00 PM IST", "5:00 PM IST", "8:00 PM IST"]


def validate_campaign_start_date(start_date):
    ist_now = get_current_ist_time()
    # Check if start_date is already a date object
    if isinstance(start_date, datetime):
        start_date = start_date.date()
    # Now we know start_date is a date object, so we can compare directly
    return start_date >= ist_now.date()
