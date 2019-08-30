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
        newDirInput = input("Enter name of new folder to create: ") 
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

lines_to_read = [0, 1, 5, 6, 7, 10, 15, 16, 17, 18, 23, 29, 30, 33]
list_of_values = []
folderToSearchName = input("Enter the name of the folder to search: ")  #Change to the cwd of the greenle bend reports output folder from Revit
searchPath = "./" + folderToSearchName
for file in os.listdir(searchPath):
    if file in newVals:
        open_file = open(cwd + '\\GREENLEE BENDS\\' + file).read()
        split_file = open_file.splitlines()
        for num in lines_to_read:
            value = split_file[num]
            if value == split_file[10]:
                split_value = value.split('       ')
                val_1 = split_value[0]
                val_2 = split_value[1].strip()
            else:                                           
                split_value = value.split(':')
                val_1 = split_value[0]
                val_2 = split_value[1].strip()
                list_of_values.append(val_2)

            
                # Append list_of values to a new text file in the appropriate folder, with a \n for each new file. This almost made my head explode! I would like to finish off this loop when I have more time tomorrow. It's getting late and I'm ready for a stiff drink!
                # shutil.copy2(searchPath + "/" + file, newDir)   # Folder needs to be in V:\\Projects\\"Job Name"\\PFS\\BEND_REPORTS
        else: continue
input("-------DONE: PRESS ENTER TO EXIT-------")