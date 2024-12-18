import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal_bonus.csv")

# to open and read csv
with open(cereal_csv) as csvfile:
    # setup a reader
    csvreader = csv.reader(csvfile, delimiter= ",")

    # the first row needs to be skipped as it contains headers
    next(csvreader)

    # work on remaining rows
    # csvreader is used to extract the contents
    # find cereals containg 5 grams of fiber or more
    # fiber is int he 8th column so index 7
    # loop through the rows in csvreader

    for row in csvreader:
        # if fiber in row [7] ? 5 we want to print the row
        if row[7] >= 5:
            print(row)
