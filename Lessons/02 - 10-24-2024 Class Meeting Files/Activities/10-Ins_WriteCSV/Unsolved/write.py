import os 
import csv
outputPath = os.path.join("..", "output", "ghosts.csv") # same as outputPath = '../output/ghosts.csv'
# use with open() to open our file in write mode and store the reference as 'csvfile'
with open(outputPath, "w", newline='') as csvfile:
    # make the csv.writer() to specify how we will make the file (use ',' as a delimiter)
    csvWriter = csv.writer(csvfile, delimiter=",")
    
    # we can use writerow() to write a row of data
    # write a header
    csvWriter.writerow(["Name", "Color"])

    # write another row of info
    csvWriter.writerow(["Inky", "Blue"])
    # write another row of info
    csvWriter.writerow(["Pinky", "Pink"])
    # write another row of info
    csvWriter.writerow(["Blinky", "Red"])
    # write another row of info
    csvWriter.writerow(["Clyde", "Orange"])