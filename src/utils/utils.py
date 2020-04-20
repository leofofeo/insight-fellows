from datetime import datetime

def get_year(date_string: str) -> int:
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    return dt.year