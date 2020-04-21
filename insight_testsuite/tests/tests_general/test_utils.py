import unittest, os
from src.utils.utils import get_year, return_sorted_list_from_product_dict
from src.processing.process_csv import process_csv_input, process_csv_output

class TestUtilityFunctions(unittest.TestCase):
    def setUp(self):
        self.test_input_file = './insight_testsuite/tests/tests_general/input/complaints.csv'
        self.test_output_file = './insight_testsuite/tests/tests_general/output/reports.csv'
        self.prod_dict = process_csv_input(self.test_input_file)

    def tearDown(self):
        file = "./insight_testsuite/tests/tests_general/output/reports.csv"
        if os.path.exists(file):
            os.remove(file)
    
    def test_get_year_successfully(self):
        test_date = "2019-04-03"
        test_date_2 = "2020-10-19"
        test_row = 1165
        return_year = get_year(test_date, test_row)
        return_year_2 = get_year(test_date_2, test_row)

        self.assertEqual(2019, return_year)
        self.assertEqual(2020, return_year_2)

    def test_get_year_unsuccessfully(self):
        test_date = "20/20/10298"
        test_row = 0
        return_year = get_year(test_date, test_row)
        self.assertEqual("", return_year)

    def test_return_sorted_list_from_product_dict(self):
        first_product_name = "credit reporting, credit repair services, or other personal consumer reports"
        first_product_year = 2019

        second_product_name = "credit reporting, credit repair services, or other personal consumer reports"
        second_product_year = 2020

        third_product_name = "debt collection"
        third_product_year = 2019

        prod_list = return_sorted_list_from_product_dict(self.prod_dict)

        self.assertEqual(type(prod_list),list)
        self.assertEqual(prod_list[0].name, first_product_name)
        self.assertEqual(prod_list[0].year, first_product_year)
        self.assertEqual(prod_list[1].name, second_product_name)
        self.assertEqual(prod_list[1].year, second_product_year)
        self.assertEqual(prod_list[2].name, third_product_name)
        self.assertEqual(prod_list[2].year, third_product_year)
