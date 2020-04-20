from processing.process_csv import process_csv_input, process_csv_output
import operator

# parse input file
csv_dict = process_csv_input()

# create and populate output file - process_csv_output returns the
# ordered list in case it needs to be used elsewher in the future
prod_list = process_csv_output(csv_dict)