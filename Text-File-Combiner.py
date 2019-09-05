#!python

import shutil, os, sys

# This portion finds the wanted text files, decodes and cleans them into a new list to be iterated through later on in the program.

while True:
    try:
        os.chdir('C:\\Users\\ggonzales\\Desktop\\Greenlee BendWorks\\Schedules of Bend Lists') # This line to be removed once program is deployed into the appropriate folder
        job_num = str(input('Enter the job number.'))
        good_list_name = input("Enter filename of text file with wanted values: " )
        good_list_name = good_list_name + ".txt"
        goodListFile = open(good_list_name, "rb").read()
        break
    except:
        print("File couldn't be opened!\nCheck your spelling.\nThis script needs to be in the same folder as the list of wanted values.\n")

mytext = goodListFile.decode('utf16')
wantedValues = mytext.splitlines()
textExtension = ".txt"
cwd = os.getcwd()

newVals = []

for line in wantedValues:
    line = line.replace('"','')
    line = line + textExtension
    newVals.append(line)

# This portion finds the project file path to save the new txt file in the correct project folder later on.

job_found = False
while not job_found:
    try:        
        for foldername, subfolders, file_names in os.walk('C:\\Users\\ggonzales\\Desktop\\VDC\\Projects\\'):    #This will have to be changed to the appropriate VDC folder        
            if job_found == True:
                break           
            for folder_name in subfolders:
                if job_num in folder_name:
                    job_dir_name = ('C:\\Users\\ggonzales\\Desktop\\VDC\\Projects\\' + folder_name)
                    job_found = True    #This staement should break the while loop. Why doesn't it?                  
                    break                
        new_dir_input = (job_dir_name + '\\3 - PFS\\Greenlee Bend Reports\\Areas to bend')              
        break
    except:
        print("\nJob not found. Restart and verify job number is typed correctly and also exists in the Projects folder.\n")
        input('Hit "Enter" key to close.')
        sys.exit()

# This portion opens a new file in the correct project directory and appends the wanted information to a txt file within it.

combined_file = open(new_dir_input + '\\Combined_' + good_list_name, 'a')
header_list = ['Project Number', 'Project Name', 'Greenlee Bender', 'Conduit Type', 'Conduit Size', 'Pipe ID', '# of Bends', 'Bend Mark', 'Bend Rotation', 'Bend Angle', 'Cut Mark 1', 'Cut Mark 2', 'Error Code\n']
combined_file.writelines(header_list)
lines_to_read = [0, 1, 5, 6, 7, 10, 15, 16, 17, 18, 23, 29, 30, 33]
search_path = ('C:\\Users\\ggonzales\\Desktop\\Greenlee BendWorks\\Exports from Revit')  # This will have to be changed to the appropriate VDC folder
list_of_values = []

for file in os.listdir(search_path):
    if list_of_values:
        combined_file.writelines('\n' + str(list_of_values))
    list_of_values = []
    if file in newVals:     
        open_file = open(search_path + '\\' + file).read()
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
                
                
        else: continue
    
combined_file.close()
input("-------DONE: PRESS ENTER TO EXIT-------")