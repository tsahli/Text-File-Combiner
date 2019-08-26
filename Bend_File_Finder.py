#!python
from io import open
import shutil
import os

print("This program will use a list of bends in .txt format and search a folder of bend reports. It will copy files that match the names on the list to a new folder.\nThis program, the list in .txt format, and a folder of .txt files must be in the same folder to run.\n")
while True:
    try:
        goodListName = raw_input("Enter filename of text file with wanted values: ")
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
        os.mkdir(cwd + "/" + newDirInput)
        break
    except:
        print("\nThis folder already exists! Use another name.\n")

newDir = cwd + "/" + newDirInput
newVals = []

for line in wantedValues:
    line = line.replace('"','')
    line = line + textExtension
    newVals.append(line)

while True:
    try:
        folderToSearchName = raw_input("Enter the name of the folder to search: ")
        searchPath = "./" + folderToSearchName
        for file in os.listdir(searchPath):
            if file in newVals:
                shutil.copy2(searchPath + "/" + file, newDir)
            else: continue
        break
    except:
        print("Directory not found!")
raw_input("-------DONE: PRESS ENTER TO EXIT-------")