#imports
import os
import csv

# parallel lists
idNumbers = [345, 678, 901]
staffNames = ["Jim", "James", "Paul"]
titles = ["Associate", "Vice President", "Director"]
yearsOfService = [5, 15, 8]
# use the zip() function to create lists with the related data in parallel lists
    # creates rows where each row in the list has the following
    # id number, staff name, title, # of years of service
employeeList = list(zip(idNumbers, staffNames, titles, yearsOfService))
# display the contents of each list (row) in the 'employeeList'
for employee in employeeList:
    print(employee)


    # make an output file in the same folder (Unsolved)
outputFile = os.path.join("output.csv") # same as outputFile = "output.csv"
#open the output file using with open() and reference as csvfile
with open(outputFile, "w", newline='') as csvfile:
    # make the writer with the "," as delimiters
    csvWriter = csv.writer(csvfile, delimiter=",")
    # write a row of header info
    csvWriter.writerow(["ID", "Name", "Title", "Years of Service"])
    # we can use .writerows() to write the data from the zipped list of tuples to the file
    csvWriter.writerows(employeeList)