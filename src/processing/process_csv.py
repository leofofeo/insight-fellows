import csv
from datetime import datetime
from models.product import (
    Product, 
    ProductNames, 
    ProductNameDoesNotExistException,
)
from models.output_row import OutputRow
from utils import utils

def process_csv_input(input_path):
    year_and_product_dict = {}
    with open(input_path) as csv_file:
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

def process_csv_output(output_path, prod_dict: dict):
    ordered_prod_list = utils.return_sorted_list_from_product_dict(prod_dict)
    with open(output_path, mode = 'w') as output_file:
        output_writer = csv.writer(output_file, delimiter=",")

        for product in ordered_prod_list:
            name = product.full_product_name
            year = product.year
            total_complaints = product.complaints
            num_of_reported_companies = product.number_of_reported_companies
            highest_percentage = product.companies.worst_company_percentage

            output_writer.writerow(
                [
                    name, 
                    year, 
                    total_complaints, 
                    num_of_reported_companies,
                    highest_percentage
                ]
            )
        
    return ordered_prod_list