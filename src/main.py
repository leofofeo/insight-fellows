from processing.process_csv import process_csv_input, process_csv_output
import operator

input_path = 'input/complaints_big.csv'
output_path = 'output/report.csv'

# parse input file
csv_dict = process_csv_input(input_path)

# create and populate output file - process_csv_output returns the
# ordered list in case it needs to be used elsewher in the future
prod_list = process_csv_output(output_path, csv_dict)