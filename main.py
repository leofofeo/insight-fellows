from src.processing.process_csv import process_csv_input, process_csv_output
import operator
import time

input_path = 'input/complaints.csv'
output_path = 'output/report.csv'

start = time.time()

csv_dict = process_csv_input(input_path)
prod_list = process_csv_output(output_path, csv_dict)

end = time.time()
print(f"Script took {end - start} seconds")
