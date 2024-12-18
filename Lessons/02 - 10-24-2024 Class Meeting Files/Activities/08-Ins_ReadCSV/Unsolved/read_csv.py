import os # allow to access data across folders in an OS
import csv # allow us to read csv

# use os.path as join()  to connect to the csv file int he resources folder
path = os.path.join("..","Resources","contacts.csv") # same as path = "../Resources/contacts.csv"

# use with open() to open the file for reading
with open(path) as csvfile: # opens the file and stores the reference as 'csvfile'
    # use the csv.reader() to specify how to delimit (separate) the data in the file
    csvreader = csv.reader(csvfile, delimiter=",")

    # we can then use csv reader to access the information from the file
    # our data in contacts.csv has header info on the first row, we can use next() in order to skip to the next
    # row, then process the rest of the data
    header = next(csvreader) #store the header
    print(header)
    # read the rest of the rows as a list of lists
    for row in csvreader:
        print(row)
