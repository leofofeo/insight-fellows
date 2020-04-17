import csv

# want to return:
# - product "all lower case"
# - year
# - total number of complaints for that product in that year
# - total number of companies receiving at least one complaint for that product and year
# - highest percentage (rounded to the nearest whoel number) of total complaints filed against one company for that product and year

"""
Model dict for data we want to return:

{
    "2019": {

    },
    "2020": {

    }
}
"""

def read_csv():
    csv_dict = {}
    with open('input/complaints.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            row