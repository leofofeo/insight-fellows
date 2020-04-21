import unittest, csv, os
from src.processing.process_csv import process_csv_input, process_csv_output
from src.models.product import Product

class TestMainFile(unittest.TestCase):
    """
    A trivial test class to ensure that "python -m unittest" is running adequately
    as folders and files are refactored and changes
    """
    def test_tests_are_running(self):
        self.assertNotEqual(3, 4)
    

class TestHandleCSV(unittest.TestCase):
    """
    Test that the reading module for reading and parsing
    CSVs does so correctly
    """

    def setUp(self):
        self.test_input_file = './insight_testsuite/tests/tests_general/input/complaints.csv'
        self.test_output_file = './insight_testsuite/tests/tests_general/output/reports.csv'
        self.prod_dict = process_csv_input(self.test_input_file)
        self.prod_list = process_csv_output(self.test_output_file, self.prod_dict)

    def tearDown(self):
        file = "./insight_testsuite/tests/tests_general/output/reports.csv"
        if os.path.exists(file):
            os.remove(file)

    def test_handle_csv_produces_the_correct_data_with_sample_complaints(self):
        with open('./insight_testsuite/tests/tests_general/input/complaints.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            expected_headers = [
                "Date received", "Product", "Sub-product", "Issue", "Sub-issue",
                "Consumer complaint narrative", "Company public response", "Company", "State", "ZIP code",
                "Tags", "Consumer consent provided?", "Submitted via", "Date sent to company", "Company response to consumer",
                "Timely response?", "Consumer disputed?", "Complaint ID"
            ]
            expected_second_row_vals = [
                "2019-09-24", "Debt collection", "I do not know", "Attempts to collect debt not owed",
                "Debt is not yours", "transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",
                "", "TRANSWORLD SYSTEMS INC", "FL", "335XX", "", "Consent provided", "Web", "2019-09-24",
                "Closed with explanation", "Yes", "N/A", "3384392",
            ]
            expected_fourth_row_vals = [
                "2020-01-06", "Credit reporting, credit repair services, or other personal consumer reports", "Credit reporting",
                "Incorrect information on your report", "Information belongs to someone else", "", "", "Experian Information Solutions Inc.",
                "CA", "92532", "", "N/A", "Email", "2020-01-06", "In progress", "Yes", "N/A", "3486776"
            ]
            expected_complaint_ids = ["3384392", "3379500", "3486776", "3416481", "3444592"]

            actual_headers = []
            actual_second_row_vals = []
            actual_fourth_row_vals = []
            actual_occupations = []
            line_count == 0
            for idx, row in enumerate(csv_reader):
                actual_occupations.append(row[-1])
                if idx == 0:
                    for col in row:
                        actual_headers.append(col)
                if line_count == 1:
                    for col in row:
                        actual_second_row_vals.append(col)
                if line_count == 3:
                    for col in row:
                        actual_fourth_row_vals.append(col)
                line_count += 1
            
            self.assertEqual(line_count, 6)
            self.assertEqual(expected_headers, actual_headers)
            self.assertEqual(expected_second_row_vals, actual_second_row_vals)
            self.assertEqual(expected_fourth_row_vals, actual_fourth_row_vals)
        
    def test_process_csv_input_returns_the_correct_dict(self):
        prod_dict = self.prod_dict
        expected_2019_credit_id = "2019Credit reporting, credit repair services, or other personal consumer reports"
        expected_2019_debit_id = "2019Debt collection"
        expected_2020_credit_id = "2020Credit reporting, credit repair services, or other personal consumer reports"
        
        # Set up expected values for the three rows in output sheet
        expected_2019_debit_product_name = "debt collection"
        expected_2019_debit_product_year = 2019
        expected_2019_debit_product_complaints = 1
        expected_2019_debit_product_company_percentage = 100.0

        expected_2019_credit_product_name = "credit reporting, credit repair services, or other personal consumer reports"
        expected_2019_credit_product_year = 2019
        expected_2019_credit_product_complaints = 3
        expected_2019_credit_product_company_percentage = 66.67

        expected_2020_credit_product_name = "credit reporting, credit repair services, or other personal consumer reports"
        expected_2020_credit_product_year = 2020
        expected_2020_credit_product_complaints = 1
        expected_2020_credit_product_company_percentage = 100.0

        # Get the actual values from the dicts
        p_2019_debit = prod_dict[expected_2019_debit_id]
        actual_2019_debit_product_name = p_2019_debit.name.lower()
        actual_2019_debit_product_year = p_2019_debit.year
        actual_2019_debit_product_complaints = p_2019_debit.complaints
        actual_2019_debit_product_company_percentage = p_2019_debit.companies.worst_company_percentage

        p_2019_credit = prod_dict[expected_2019_credit_id]
        actual_2019_credit_product_name = p_2019_credit.name.lower()
        actual_2019_credit_product_year = p_2019_credit.year
        actual_2019_credit_product_complaints = p_2019_credit.complaints
        actual_2019_credit_product_company_percentage = p_2019_credit.companies.worst_company_percentage

        p_2020_credit = prod_dict[expected_2020_credit_id]
        actual_2020_credit_product_name = p_2020_credit.name.lower()
        actual_2020_credit_product_year = p_2020_credit.year
        actual_2020_credit_product_complaints = p_2020_credit.complaints
        actual_2020_credit_product_company_percentage = p_2020_credit.companies.worst_company_percentage

        self.assertIn(expected_2019_credit_id, prod_dict)
        self.assertIn(expected_2019_debit_id, prod_dict)
        self.assertIn(expected_2020_credit_id, prod_dict)

        self.assertEqual(expected_2019_debit_product_name, actual_2019_debit_product_name)
        self.assertEqual(expected_2019_debit_product_year, actual_2019_debit_product_year)
        self.assertEqual(expected_2019_debit_product_complaints, actual_2019_debit_product_complaints)
        self.assertEqual(expected_2019_credit_product_company_percentage, actual_2019_credit_product_company_percentage )

        self.assertEqual(expected_2019_credit_product_name, actual_2019_credit_product_name)
        self.assertEqual(expected_2019_credit_product_year, actual_2019_credit_product_year)
        self.assertEqual(expected_2019_credit_product_complaints, actual_2019_credit_product_complaints)
        self.assertEqual(expected_2019_credit_product_company_percentage, actual_2019_credit_product_company_percentage)

        self.assertEqual(expected_2020_credit_product_name, actual_2020_credit_product_name)
        self.assertEqual(expected_2020_credit_product_year, actual_2020_credit_product_year)
        self.assertEqual(expected_2020_credit_product_complaints, actual_2020_credit_product_complaints)
        self.assertEqual(expected_2020_credit_product_company_percentage, actual_2020_credit_product_company_percentage)

    def test_process_csv_out_returns_correctly_ordered_list(self):
        prod_list = self.prod_list
        actual_first_product = prod_list[0]
        actual_second_product = prod_list[1]
        actual_third_product = prod_list[2]

        self.assertEqual(type(actual_first_product), Product)
        self.assertEqual(type(actual_second_product), Product)
        self.assertEqual(type(actual_third_product), Product)

        expected_first_product_name = "credit reporting, credit repair services, or other personal consumer reports"
        expected_first_product_year = 2019
        expected_first_product_total_complaints = 3
        expected_first_product_percentage = 66.67

        expected_second_product_name = "credit reporting, credit repair services, or other personal consumer reports"
        expected_second_product_year = 2020
        expected_second_product_total_complaints = 1
        expected_second_product_percentage = 100.0

        expected_third_product_name = "debt collection"
        expected_third_product_year = 2019
        expected_third_product_total_complaints = 1
        expected_third_product_percentage = 100.0

        self.assertEqual(expected_first_product_name, actual_first_product.name)
        self.assertEqual(expected_first_product_year, actual_first_product.year)
        self.assertEqual(expected_first_product_total_complaints, actual_first_product.complaints)
        self.assertEqual(expected_first_product_percentage, actual_first_product.companies.worst_company_percentage)

        self.assertEqual(expected_second_product_name, actual_second_product.name)
        self.assertEqual(expected_second_product_year, actual_second_product.year)
        self.assertEqual(expected_second_product_total_complaints, actual_second_product.complaints)
        self.assertEqual(expected_second_product_percentage, actual_second_product.companies.worst_company_percentage)

        self.assertEqual(expected_third_product_name, actual_third_product.name)
        self.assertEqual(expected_third_product_year, actual_third_product.year)
        self.assertEqual(expected_third_product_total_complaints, actual_third_product.complaints)
        self.assertEqual(expected_third_product_percentage, actual_third_product.companies.worst_company_percentage)

    def test_process_csv_out_writes_to_file_correctly(self):
        rows = {
            "row_1": [],
            "row_2": [],
            "row_3": [],
        }

        with open(self.test_output_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            for idx, row in enumerate(csv_reader):
                row_name = "row_" + str(idx + 1)
                for col in row:
                    rows[row_name].append(col)


        row_1_col_1 = "credit reporting, credit repair services, or other personal consumer reports"
        row_1_col_2 = "2019"
        row_1_col_3 = "3"
        row_1_col_4 = "2"
        row_1_col_5 = "66.67"

        row_2_col_1 = "credit reporting, credit repair services, or other personal consumer reports"
        row_2_col_2 = "2020"
        row_2_col_3 = "1"
        row_2_col_4 = "1"
        row_2_col_5 = "100.0"

        row_3_col_1 = "debt collection"
        row_3_col_2 = "2019"
        row_3_col_3 = "1"
        row_3_col_4 = "1"
        row_3_col_5 = "100.0"
        
        self.assertEqual(rows["row_1"][0], row_1_col_1)
        self.assertEqual(rows["row_1"][1], row_1_col_2)
        self.assertEqual(rows["row_1"][2], row_1_col_3)
        self.assertEqual(rows["row_1"][3], row_1_col_4)
        self.assertEqual(rows["row_1"][4], row_1_col_5)
        self.assertEqual(rows["row_2"][0], row_2_col_1)
        self.assertEqual(rows["row_2"][1], row_2_col_2)
        self.assertEqual(rows["row_2"][2], row_2_col_3)
        self.assertEqual(rows["row_2"][3], row_2_col_4)
        self.assertEqual(rows["row_2"][4], row_2_col_5)
        self.assertEqual(rows["row_3"][0], row_3_col_1)
        self.assertEqual(rows["row_3"][1], row_3_col_2)
        self.assertEqual(rows["row_3"][2], row_3_col_3)
        self.assertEqual(rows["row_3"][3], row_3_col_4)
        self.assertEqual(rows["row_3"][4], row_3_col_5)
