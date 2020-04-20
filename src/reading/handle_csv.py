import csv
from datetime import datetime
# want to return:
# - product "all lower case"
# -- Product class
# --- no. of complaints (below) counter property
# --- no. of companies receiving complaint for that product and year (set)
# - year
# - total number of complaints for that product in that year
# - highest percentage (rounded to the nearest whoel number) of total complaints filed against one company for that product and year
# -- calculated property

"""
Model dict for data we want to return:

{
    "2019": {
        dict of product class where the key is a shorthand for the product name, and the class contains the information listed above
        and total number of complaints for each class is a property on that object
    },
    "2020": {

    }
}
"""
year_dict = {}
products = []
product_ids = []

class Product:

    def __init__(self, product_name, year):
        self.year = year
        self.reported_companies = set()
        self.set_name(product_name)
        self.complaints = 0
    
    def set_name(self, product_name):
        try:
            self.name = ProductNames.get_product_name_symbol(product_name)
        except ProductNames.ProductNameDoesNotExistException:
            print(f"Unable to extract product name for row {idx}")
            shorted_name = ""

class ProductNames:
    names = ["debt collection", "credit reporting, credit repair services, or other personal consumer reports"]
    product_names = {
        "debt": names[0],
        "credit": names[1],
    }

    @classmethod
    def get_product_name_symbol(product_name: str) -> str:
        symbol = ""
        if product_name.lower() not in names:
                raise ProductNames.ProductNameDoesNotExistException()
        if product_name == product_names["debt"]:
            symbol = "debt"
        elif product_name == product_name["credit"]:
            symbol = "credit"
        return symbol
    @classmethod
    class ProductNameDoesNotExistException(Exception):
        """Product name doesn't exist"""

def get_year(date_string: str) -> int:
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    return dt.year

def read_csv():
    csv_dict = {}
    with open('input/complaints.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for idx, row in enumerate(csv_reader):
            if idx == 0:
                continue
            try:
                year = get_year(row[0])
            except ValueError:
                print(f"Unable to extract year for row {idx}")
                year = ""

            try:
                shortened_name = ProductNames.get_product_name_symbol(row[1])
            except ProductNames.ProductNameDoesNotExistException:
                print(f"Unable to extract product name for row {idx}")
                shorted_name = ""

        