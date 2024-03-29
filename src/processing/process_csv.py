import csv
from datetime import datetime
from src.models.product import (
    Product,
    ProductNames,
    ProductNameDoesNotExistException
)
from src.utils import utils

def process_csv_input(input_path):
    year_and_product_dict = {}
    with open(input_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for idx, row in enumerate(csv_reader):
            if idx == 0:
                continue
           
            year = utils.get_year(row[0], idx)
            name = row[1].lower()
            product_id = str(year) + name

            if product_id in year_and_product_dict:
                product = year_and_product_dict[product_id]
            else:
                product = Product(name, year, product_id)
                year_and_product_dict[product.product_id] = product

            company = row[7].lower()
            product.reported_companies.add(company)
            product.complaints += 1
            product.companies.add_company_complaint(company)

    return year_and_product_dict

def process_csv_output(output_path, prod_dict):
    ordered_prod_list = utils.return_sorted_list_from_product_dict(prod_dict)
    with open(output_path, mode = 'w') as output_file:
        output_writer = csv.writer(output_file, delimiter=",")

        for product in ordered_prod_list:
            name = product.name
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