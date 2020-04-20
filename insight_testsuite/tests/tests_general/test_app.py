import unittest, csv
from src.reading import handle_csv

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
    def test_handle_csv_produces_the_correct_data_with_sample_input(self):
        with open('./insight_testsuite/tests/tests_general/input/sample_input.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            expected_headers = [
                "First Name",
                "Last Name",
                "Occupation",
                "State",
            ]
            expected_second_row_vals = [
                "Leo", "Rubiano", "Software Engineer", "Minnesota"
            ]
            expected_fourth_row_vals = [
                "Jane", "Doe", "Product Manager", "Massachusetts"
            ]
            expected_occupations = ["Software Engineer", "Writer", "Product Manager"]

            actual_headers = []
            actual_second_row_vals = []
            actual_fourth_row_vals = []
            actual_occupations = []
            line_count == 0
            for idx, row in enumerate(csv_reader):
                actual_occupations.append(row[2])
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
            
            self.assertEqual(line_count, 4)
            self.assertEqual(expected_headers, actual_headers)
            self.assertEqual(expected_second_row_vals, actual_second_row_vals)
            self.assertEqual(expected_fourth_row_vals, actual_fourth_row_vals)

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
        pass