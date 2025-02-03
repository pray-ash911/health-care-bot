from datetime import datetime

def format_time_input(time_str):
    try:
        return datetime.strptime(time_str, '%H:%M').strftime('%I:%M %p')
    except ValueError:
        return None  # Handle invalid time format
