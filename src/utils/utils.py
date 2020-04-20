from datetime import datetime
from models.product import ProductNames, ProductNameDoesNotExistException

def get_year(date_string: str, idx: int) -> int:
    year = ""
    try:
        dt = datetime.strptime(date_string, "%Y-%m-%d")
        year = dt.year
    except ValueError:
        print(f"Unable to extract year for row {idx}")
    return year


# Get the "symbol" of the longer product name for readability
def get_shortened_name_symbol(name_string: str, idx: int) -> str:
    shortened_name = ""
    try:
        shortened_name = ProductNames.get_product_name_symbol(name_string)
    except ProductNameDoesNotExistException:
        print(f"Unable to extract product name for row {idx}")
    
    return shortened_name