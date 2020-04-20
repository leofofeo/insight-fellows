import csv
from datetime import datetime
from models.product import (
    Product, 
    ProductNames, 
    ProductNameDoesNotExistException,
)
from utils import utils

def process_csv_input():
    year_and_product_dict = {}
    with open('input/complaints.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for idx, row in enumerate(csv_reader):
            if idx == 0:
                continue
           
            year = utils.get_year(row[0], idx)
            name_symbol = utils.get_shortened_name_symbol(row[1], idx)

            product_id = str(year) + name_symbol

            # Build out or enhance a dictionary of products identified by 
            # their unique product name and year
            if product_id in year_and_product_dict:
                product = year_and_product_dict[product_id]
            else:
                product = Product(name_symbol, year, product_id)
                year_and_product_dict[product.product_id] = product

            company = row[7]
            product.reported_companies.add(company.lower())
            product.complaints += 1
            product.companies.add_company_complaint(company)

    return year_and_product_dict
