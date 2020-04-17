import csv

# want to return:
# - product "all lower case"
# -- Product class
# --- no. of complaints (below) counter property
# --- no. of companies receiving complaint for that product and year (set)
# - year
# - total number of complaints for that product in that year
# - highest percentage (rounded to the nearest whoel number) of total complaints filed against one company for that product and year
# -- calculated property

"""
Model dict for data we want to return:

{
    "2019": {
        dict of product class where the key is a shorthand for the prodcut name, and the class contains the information listed above
        and total number of complaints for each class is a property on that object
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