from reading.handle_csv import read_csv

# parse input file
csv_dict = read_csv()
for k in csv_dict:
    print(f"Key: {k}")
    print(f"Product object: {csv_dict[k]}")
    print("Full name: ", csv_dict[k].full_product_name)

# create report file