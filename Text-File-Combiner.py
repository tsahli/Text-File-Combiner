#!python
from io import open
import shutil
import os

# This portion finds the wanted text files and copies them into a new folder that the user designates

while True:
    try:
        goodListName = input("Enter filename of text file with wanted values: ")
        goodListName = goodListName + ".txt"
        goodListFile = open(goodListName, "rb").read()
        break
    except:
        print("File couldn't be opened!\nCheck your spelling.\nThis script needs to be in the same folder as the list of wanted values.\n")

mytext = goodListFile.decode('utf16')
wantedValues = mytext.splitlines()
textExtension = ".txt"
cwd = os.getcwd()

while True:
    try:
        newDirInput = raw_input("Enter name of new folder to create: ") 
        os.mkdir(cwd + "/" + newDirInput)   # Folder needs to be in V:\\Projects\\"Job Name"\\PFS\\BEND_REPORTS
        break
    except:
        print("\nThis folder already exists! Use another name.\n")

newDir = cwd + "/" + newDirInput    # Folder needs to be in V:\\Projects\\"Job Name"\\PFS\\BEND_REPORTS
newVals = []

for line in wantedValues:
    line = line.replace('"','')
    line = line + textExtension
    newVals.append(line)

while True:
    lines_to_read = [0, 1, 5, 6, 7, 10, 15, 16, 18, 20, 27, 33, 34, 37]
    list_of_values = []
    folderToSearchName = raw_input("Enter the name of the folder to search: ")  #Change to the cwd of the greenle bend reports output folder from Revit
    searchPath = "./" + folderToSearchName
    for file in os.listdir(searchPath):
        if file in newVals:
            os.open(file).read()
            # os.open('write_file', 'a')
            # write_file.append
            open_file = file.splitlines()
            for num in lines_to_read:
                value = file[num]
                if value == file[10]:
                    val_1, val_2 = value.split('  ')
                else:                                           
                    val_1, val_2 = value.split(':')
                list_of_values.append(val_2)

            
                # Append list_of values to a new text file in the appropriate folder, with a \n for each new file. This almost made my head explode! I would like to finish off this loop when I have more time tomorrow. It's getting late and I'm ready for a stiff drink!
                shutil.copy2(searchPath + "/" + file, newDir)   # Folder needs to be in V:\\Projects\\"Job Name"\\PFS\\BEND_REPORTS
        else: continue
raw_input("-------DONE: PRESS ENTER TO EXIT-------")