import operator
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

def get_shortened_name_symbol(name_string: str, idx: int) -> str:
    """Get the "symbol" of the longer product name for readability"""
    
    shortened_name = ""
    try:
        shortened_name = ProductNames.get_product_name_symbol(name_string)
    except ProductNameDoesNotExistException:
        print(f"Unable to extract product name for row {idx}")
    
    return shortened_name

def return_sorted_list_from_product_dict(prod_dict: dict) -> list:
    prod_list = [prod for prod in prod_dict.values()]
    ordered_list = sorted(prod_list, key=operator.attrgetter("name", "year"))
    return ordered_list