#!python3
#Text-File-Combiner.py - This program will search through txt files and combine the right information from each one into a csv file for further processing
#The user name in the search path variable will need to be changed to the correct file path that it is being copied into!

import os, sys, csv, getpass

# This portion finds the wanted text files, decodes and cleans them into a new list to be iterated through later on in the program.

user = getpass.getuser()

while True:
    try:
        os.chdir('V:\\1. VDC Projects\\Greenlee_Bend_Reports\\' + user + '\\Lists_of_wanted_Bends')  # This line to be removed once program is deployed into the appropriate folder
        job_num = str(input('Enter the job number: '))
        good_list_name = input("Enter filename of text file with wanted values: " )
        good_list_name_txt = good_list_name + ".txt"
        goodListFile = open(good_list_name_txt, "rb").read()
        break
    except:
        print("File couldn't be opened!\nCheck your spelling.\nThis script needs to be in the same folder as the list of wanted values.\n")

mytext = goodListFile.decode('utf16')
wantedValues = mytext.splitlines()
textExtension = ".txt"
cwd = os.getcwd()   #Is this used anywhere?

newVals = []

for line in wantedValues:
    line = line.replace('"','')
    line = line + textExtension
    newVals.append(line)

# This portion finds the project file path to save the new txt file in the correct project folder later on.

projects_dir_path = ('V:\\1. VDC Projects')
projects_dir = os.listdir(projects_dir_path)
good_bends_dir = ('\\3- PFS\\Greenlee_Used_Bend_Reports')

job_found = False
while not job_found:
    try:        
        for dir_names in projects_dir:            
            if job_found == True:
                break           
            else:
               if job_num in dir_names:                
                   job_dir_name = (projects_dir_path + '\\' + dir_names)
                   job_name = str(job_dir_name.split(' - ')[1])
                   job_found = True    #This staement should break the while loop. Why doesn't it?
                   break            
            
        new_dir_input = (job_dir_name + good_bends_dir)              
        break
    except:
        print("\nJob not found. Restart and verify job number is typed correctly and also exists in the Projects folder.\n")
        input('Hit "Enter" key to close.')
        sys.exit()

# This portion opens a new file in the correct project directory and appends the wanted information to a txt file within it.

job_header_list_1 = ['Job Name', 'Job Number']
job_header_list_2 = [job_name, job_num]
param_header_list = ['Conduit Type', 'Conduit Size', 'Pipe ID', '# of Bends','Cut Mark 1', 'Cut Mark 2', 'Bend Mark', 'Bend Rotation', 'Bend Angle','# of Conc. Bends', 'Error Code']
lines_to_read = [6, 7, 10, 15, 29, 30, 16, 17, 18, 23, 33]
search_path = ('V:\\1. VDC Projects\\Greenlee_Bend_Reports\\' + user + '\\BendWorks_Exports') # The user name will have to be changed to the same name of the folder path VDC folder

csvPath = new_dir_input + '\\Combined_' + good_list_name + '.csv'

with open(csvPath, 'a', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(job_header_list_1)
    writer.writerow(job_header_list_2) 
    writer.writerow(param_header_list)
    writer.writerow('')

for file in os.listdir(search_path):
    if file in newVals:     
        open_file = open(search_path + '\\' + file).read()
        split_file = open_file.splitlines()
        list_of_values = []
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
        with open(csvPath, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(list_of_values)

input("-------DONE: PRESS ENTER TO EXIT-------")