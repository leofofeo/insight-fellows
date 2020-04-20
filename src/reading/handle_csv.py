import csv
from datetime import datetime
from models.product import (
    Product, 
    ProductNames, 
    ProductNameDoesNotExistException,
)
from utils.utils import get_year

def read_csv():
    year_and_product_dict = {}
    with open('input/complaints.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for idx, row in enumerate(csv_reader):
            if idx == 0:
                continue

            # Get the year
            try:
                year = get_year(row[0])
            except ValueError:
                print(f"Unable to extract year for row {idx}")
                year = ""

            # Get the "symbol" of the longer product name for readability
            try:
                shortened_name = ProductNames.get_product_name_symbol(row[1])
            except ProductNameDoesNotExistException:
                print(f"Unable to extract product name for row {idx}")
                shortened_name = ""

            product_id = str(year) + shortened_name

            # Build out or enhance a dictionary of products identified by 
            # their unique product name and year
            if product_id in year_and_product_dict:
                product = year_and_product_dict[product_id]
            else:
                product = Product(shortened_name, year, product_id)
                year_and_product_dict[product.product_id] = product

            company = row[7]
            product.reported_companies.add(company.lower())
            product.complaints += 1
            product.companies.add_company_complaint(company)

    return year_and_product_dict
