from processing.process_csv import process_csv_input, process_csv_output
import operator

# parse input file
csv_dict = process_csv_input()
# for k in csv_dict:
#     print(f"Key: {k}")
#     print(f"Product object: {csv_dict[k]}")

# create report file
prod_list = process_csv_output(csv_dict)