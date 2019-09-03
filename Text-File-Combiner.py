#!python
from io import open
import shutil
import os

# This portion finds the wanted text files and copies them into a new folder that the user designates

while True:
    try:
        os.chdir('C:\\Users\\ggonzales\\Desktop\\Greenlee BendWorks\\Schedules of Bend Lists')
        job_num = str(input('Enter the job number.'))
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

job_found = False

while not job_found:
    try:
        #subfolders = os.walk('C:\\Users\\ggonzales\\Desktop\\VDC\\Projects\\')
        for foldername, subfolders, file_names in os.walk('C:\\Users\\ggonzales\\Desktop\\VDC\\Projects\\'):
            if job_found == True:
                break
            for folder_name in subfolders:
                if job_num in folder_name:
                    job_dir_name = ('C:\\Users\\ggonzales\\Desktop\\VDC\\Projects\\' + folder_name)
                    job_found = True
                    break
                else:
                    print('Job folder not found')
        new_dir_input = (job_dir_name + '\\3 - PFS\\Greenlee Bend Reports\\Areas to bend')
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

header_list = ['Project Number', 'Project Name', 'Greenlee Bender', 'Conduit Type', 'Conduit Size', 'Pipe ID', '# of Bends', 'Bend Mark', 'Bend Rotation', 'Bend Angle', 'Cut Mark 1', 'Cut Mark 2', 'Error Code\n']
lines_to_read = [0, 1, 5, 6, 7, 10, 15, 16, 17, 18, 23, 29, 30, 33]
list_of_values = []
folderToSearchName = input("Enter the name of the folder to search: ")  #Change to the cwd of the greenle bend reports output folder from Revit
searchPath = "./" + folderToSearchName
#combined_file = open(new_dir_input, 'a')
#combined_file.append(header_list)

for file in os.listdir(searchPath):
    if file in newVals:
        open_file = open(cwd + '\\GREENLEE BENDS\\' + file).read()
        split_file = open_file.splitlines()
        if job_num in str(split_file[0]):
            for num in lines_to_read:
                value = split_file[num]
                if value == split_file[10]:
                    split_value = value.split('       ')
                    val_1 = split_value[0]
                    val_2 = split_value[1].strip()
                    list_of_values.append(val_2)
                else:                                           
                    split_value = value.split(':')
                    val_1 = split_value[0]
                    val_2 = split_value[1].strip()
                    list_of_values.append(val_2)
            
                # Append list_of values to a new text file in the appropriate folder, with a \n for each new file. This almost made my head explode! I would like to finish off this loop when I have more time tomorrow. It's getting late and I'm ready for a stiff drink!
                # shutil.copy2(searchPath + "/" + file, newDir)   # Folder needs to be in V:\\Projects\\"Job Name"\\PFS\\BEND_REPORTS
        else: continue
    combined_file.append(list_of_values, '\n')
input("-------DONE: PRESS ENTER TO EXIT-------")