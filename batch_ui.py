from load_data import load_data, add_average #Imports the load_data and add_average functions 
import sort_plot as sp #Imports sort plot as sp
from optimization import minimum, maximum #Imports the minimum and maximum functions 

file_name = input("Please enter the name of the file where your commands are stored: ") #Prompts the user for the name of the text file with the commands
opened_file = open(file_name, 'r') #Opens the text file
read_file = opened_file.readlines() #Reads the text file and saves it to a variable
opened_file.close() #Closes the text file

command_list = [] #Creates an empty list for the commands
personalized_output = {'Health': '', 'Failures': 'Failures', 'StudyTime': 'Hours', 'Absences': 'Absences', 'Age': 'years old'} #Sets the message to be displayed for each attribute

for command in read_file: #Sets each line in the text file to a list and puts them all inside one list
    command_list.append(command.split())

for command_lists in command_list: #Runs through each line of commands
    if command_lists[0] == 'L;' or command_lists[0] == 'l;': #If the command is L or l, then load the data
        print('Data loaded')
        data_file_name = command_lists[1] #Save the filename from the command
    if command_lists[0] == 'Q;' or command_lists[0] == 'q;': #If the command is Q or q, then exit the program
        exit()

    if command_lists[0] == 'S' or command_lists[0] == 's': #If the command is S or s, then sort the data based on the attribute given in the command
        print('Data sorted.')
        sorted_data = add_average(load_data(data_file_name, command_lists[1])) #Save the sorted data to another variable
        if command_lists[2] != 'N' and command_lists[2] != 'n': #Additionally, if the attribute has N right after it, then the sorted data will not be printed
            print(sorted_data)

    if command_lists[0] == 'H' or command_lists[0] == 'h': #If the command is H or h, then a histogram of the sorted data will be displayed
        sp.histogram(sorted_data, command_lists[1])

    if command_lists[0] == 'B' or command_lists[0] == 'b': #If the command is B or b, then the highest value in the dictionary will be printed
        max1 = maximum(sorted_data, command_lists[1])
        max = max1[0]
        print('The best value for the attribute', command_lists[1], 'is', max, personalized_output[command_lists[1]]) 
        
    if command_lists[0] == 'W' or command_lists[0] == 'w': #If the command is W or w, then the lowest value in the dictionary will be printed
        min1 = minimum(sorted_data, command_lists[1])
        min = min1[0]
        print('The worse value for the attribute', command_lists[1], 'is', min, personalized_output[command_lists[1]])
        
    else: #If the command did not match any of the above then the program will not recognize it
        print('That is not a valid command')






