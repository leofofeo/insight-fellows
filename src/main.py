from reading.handle_csv import read_csv

# parse input file
csv_dict = read_csv()
for k in csv_dict:
    print(f"Key: {k}")
    print(f"Product object: {csv_dict[k]}")

# create report file