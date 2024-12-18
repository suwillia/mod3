# store the file path that goes from 'Unsolved' to 'Resources' then to input.txt file
file = "../Resources/input.txt" # .. -> goes up one folder
                                # /Resources -> goes into the 'Resources folder'
                                # 'input.txt' is the file that we want to access
# open the file in read mode and save the reference to the opened file as 'text'
with open(file, 'r') as text:
    # store all of the lines from the text file using .read()
    lines = text.read()
    # print all of the contents at once to the console
    print(lines)