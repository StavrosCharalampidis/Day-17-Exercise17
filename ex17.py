# Import from sys the argv module
from sys import argv

# This import is for check if the file exist
from os.path import exists

# Those args is input from the terminal
script, inputFile, outputFile = argv

# Print in f-string double single quotes the script name and the file names
print(f'from the script {script}, the input file is {inputFile} and the output is {outputFile}')

# The var inFile store a method to open file in read mode
inFile = open(inputFile, "r")

# Print if the file is exist print true else false
print(f'the output file must to exist {exists(outputFile)} ')

# if true press okey or something else ctrl + c
input('>')

# The var inFile store a method to open file in write mode
outFile = open(outputFile, "w")

# This Method is for write in to file 
outFile.write(inFile.read())

# Print for done
print("Done !!!")

# Close the files
inFile.close()
outFile.close()