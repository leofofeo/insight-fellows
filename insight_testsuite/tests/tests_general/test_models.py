import unittest
from src.models.product import Product
from src.models.companies import Companies

class TestProductModel(unittest.TestCase):
    def test_instantiation(self):
        name = "debt collection"
        year = 2019
        product_id = str(year) + name
        
        product = Product(name, year)
        product.complaints += 1
        product.complaints += 1
        product.complaints += 1

        self.assertEqual(name, product.name)
        self.assertEqual(year, product.year)
        self.assertEqual(product_id, product.product_id)
        self.assertEquals(3, product.complaints)

    def test_number_of_reported_companies(self):
        name = "credit reporting, credit repair services, or other personal consumer reports"
        year = 2020
        product_id = str(year) + name
        product = Product(name, year)

        self.assertEqual(product_id, product.product_id)

        companies = ["acme", "acme", "transunion", "experian", "transunion"]
        for company in companies:
            product.reported_companies.add(company)
        self.assertEqual(3, len(product.reported_companies))
        self.assertIn("acme", product.reported_companies)
        self.assertIn("transunion", product.reported_companies)
        self.assertIn("experian", product.reported_companies)
        

class TestCompaniesModel(unittest.TestCase):
    
    def setUp(self):
        self.companies = Companies()

    def test_companies_data(self):
        offending_companies = ["acme", "ACME", "exPERian", "experian", "acme", "Transunion"]
        for company in offending_companies:
            self.companies.add_company_complaint(company)
        
        companies_data = self.companies.companies_data
        
        self.assertEqual(len(companies_data), 3)
        
        self.assertIn("acme", companies_data)
        self.assertIn("transunion", companies_data)
        self.assertIn("experian", companies_data)

        self.assertEqual(companies_data["experian"], 2)
        self.assertEqual(companies_data["transunion"], 1)
        self.assertEqual(companies_data["acme"], 3)

    def test_worst_company_percentage(self):
        offending_companies = ["acme", "ACME", "exPERian", "experian", "acme", "Transunion"]
        for company in offending_companies:
            self.companies.add_company_complaint(company)
        
        expected_percentage = 50.0 # acme ic currently 3 of 6 complaints
        actual_percentage = self.companies.worst_company_percentage

        self.assertEqual(expected_percentage, actual_percentage)

        self.companies.add_company_complaint("experian")
        self.companies.add_company_complaint("experian")
        self.companies.add_company_complaint("experian")
        self.companies.add_company_complaint("experian")

        new_expected_percentage = 60.0
        actual_percentage = self.companies.worst_company_percentage

        self.assertEqual(new_expected_percentage, actual_percentage)
