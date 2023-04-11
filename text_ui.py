import sort_plot as sp
import optimization as op
from load_data import load_data, add_average

commands = ["L)", "S)", "H)", "W)", "B)", "Q)", "l)", "s)", "h)", "w)", "b)", "q)"] 

def get_input():
    """Gets an input from user and displays list of commands. 
    >>>get_input()
    The available commands are:

    1. L)oad Data

    2. S)ort Data
    'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 'G1' 'G2' 'G3' 'G_Avg'

    3. H)istogram
    'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'

    4. W)orst _____ for Grades
    'Age' 'StudyTime' 'Failures' 'Health' 'Absences'

    5. B)est _____ for Grades
    'Age' 'StudyTime' 'Failures' 'Health' 'Absences'

    6. Q)uit

    Please type your command:<user inputed command here>


    """
    line1 = "The available commands are:" #lines that will be printed many of times
    option1 = "1. L)oad Data"
    option2 = "2. S)ort Data \n'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 'G1' 'G2' 'G3' 'G_Avg'" 
    option3 = "3. H)istogram \n'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'" 
    option4 = "4. W)orst _____ for Grades\n 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'"
    option5 = "5. B)est _____ for Grades\n 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'" 
    option6 =  "6. Q)uit"
    
    lis = [option1,option2, option3, option4, option5, option6] #prints the lines above
    print(line1, "\n")
    for i in lis:
        print(i, "\n") 
    
    inpu = input("Please type your command:") #gets input from user
    return inpu

def screen(inpu: str):
    """Takes an input from user using get_input() string type and returns data based on the string command.
    Preconditions: inpu must == one of the following ("L)", "S)", "H)", "W)", "B)", "Q)", "l)", "s)", "h)", "w)", "b)", "q)")
    
    >>>screen("L)")
    Please enter the name of the file:<user input> 
    Please enter the attribute to use as key: <user input>
    Data Loaded
    <or if inavlid attribute>
    Invaalid Key
    """
    qui = False #tells program when to quit
    data_loaded = False #tells when 
    load_datas = None #dictionary for future
    
    while qui == False: #this makes a loop that redoes the commands until quit command is entered
        qui = True #so it doesnt make infnite outputs 
        
        if inpu == commands[0] or inpu == commands[6]: #command l) loads the data
            file = input("\nPlease enter the name of the file: ")
            attribute101 = input("\nPlease enter the attribute to use as key: ")
            load_datas = add_average(load_data(file, attribute101))
            while load_datas == "Invalid Key":

                print("\nInvalid Key")
                attribute101 = input("Please enter the attribute to use as key: ")
                load_datas = add_average(load_data(file, attribute101))
            print("\nData Loaded\n")
            qui = False
            data_loaded = True
            inpu = get_input()
            
            
        elif inpu == commands[1] or inpu == commands[7]: #command S) sorts the data to be viewed easier
            attribute_list = ['School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences' ,'G1', 'G2' ,'G3', 'G_Avg'] #all possible inputs
            if data_loaded == True:#checks if l) command has been run as it has to be, the else prints error
                
                print("\nPlease enter the attribute you want to use for sorting:\n", 
                      "'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 'G1' 'G2' 'G3' 'G_Avg'")
                
                attribute101 = input("\n: ") #gets how they want to organize it
               
                while attribute101 not in attribute_list:
                    if attribute101 not in attribute_list: #if they give an answer not in the attribute_list prints error and asks for it again
                        attribute101 = input("\nPlease enter valid Attribute from above list: ")
                    
                data_sorted = sp.sort_students_bubble(load_datas, attribute101) #sorts the data using imported command
                display_data = (input("\nData Sorted. Do you want to display data?: ")) #asks if it wants to be displayed
                if display_data == 'y' or display_data == 'yes' or display_data == "Yes" or display_data == "Y":
                    print(data_sorted)
                
            else:
                print("File not loaded, please load a file first.")
            qui = False
            inpu = get_input()
            
        elif inpu == commands[2] or inpu ==  commands[8]: #makes histogram command H)
            attribute_list = ['School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences']#all possible inputs
            if data_loaded == True:#checks if l) command has been run as it has to be, the else prints error
                
                print("\nPlease enter the attribute you want to use for histogram:\n", 
                      "'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'")
                
                attribute101 = input("\n: ")
                
                while attribute101 not in attribute_list:
                    if attribute101 not in attribute_list: #if they give an answer not in the attribute_list prints error and asks for it again
                        attribute101 = input("\nPlease enter valid Attribute from above list: ") 
                
                sp.histogram(load_datas, attribute101) #makes and shows histogram
                
            else:
                print("File not loaded, please load a file first.")
            qui = False
            inpu = get_input()
                
        elif inpu == commands[3] or inpu == commands[9]:#shows worst of data
            string = "The worse value for attribute"
            attribute_list = ['School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences']#all possible inputs
            if data_loaded == True:#checks if l) command has been run as it has to be, the else prints error
                print("Please enter the attribute you want to calculate the worst value of the attribute for in terms of grades:")
                print("\n'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'")
                
                attribute101 = input("\n: ")
                
                while attribute101 not in attribute_list:
                    if attribute101 not in attribute_list: #if they give an answer not in the attribute_list prints error and asks for it again
                        attribute101 = input("\nPlease enter valid Attribute from above list: ")
                    
                worst = op.minimum(load_datas, attribute101) #finds the worse and unpacks it
                x, y = worst
                x = round(x)
                
                
                
                if attribute101 == attribute_list[1]: #checks which attribute it is and prints a statement accordingly
                    print(string, attribute101, f"is {x} Years old")
                elif attribute101 == attribute_list[0]: 
                    print(string, attribute101, f"is the school {x}")
                elif attribute101 == attribute_list[2]:
                    print(string, attribute101, f"{x} Hours")
                elif attribute101 == attribute_list[3]:
                    print(string, attribute101, f"{x} amount of failures")
                elif attribute101 == attribute_list[4]:
                    print(string, attribute101, f"{x} health")
                elif attribute101 == attribute_list[5]:
                    print(string, attribute101, f"{x} amount of absences")
                
            else:
                print("File not loaded, please load a file first.")
            qui = False
            inpu = get_input()   
            
            
        elif inpu == commands[4] or inpu == commands[10]: #shows best of data
            string = "The best value for attribute"
            attribute_list = ['School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences']#all possible inputs
            if data_loaded == True:#checks if l) command has been run as it has to be, the else prints error
                print("Please enter the attribute you want to calculate the best value of the attribute for in terms of grades:")
                print("\n'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'")
                
                attribute101 = input("\n: ")
                
                while attribute101 not in attribute_list:
                    if attribute101 not in attribute_list: #if they give an answer not in the attribute_list prints error and asks for it again
                        attribute101 = input("\nPlease enter valid Attribute from above list: ")
                
                best = op.maximum(load_datas, attribute101) #finds the best and unpacks it
                x, y = best
                x = round(x)
                
                
                
                if attribute101 == attribute_list[1]: #checks which attribute it is and prints a statement accordingly
                    print(string, attribute101, f"is {x} Years old")
                elif attribute101 == attribute_list[0]: 
                    print(string, attribute101, f"is the school {x}")
                elif attribute101 == attribute_list[2]:
                    print(string, attribute101, f"{x} Hours")
                elif attribute101 == attribute_list[3]:
                    print(string, attribute101, f"{x} amount of failures")
                elif attribute101 == attribute_list[4]:
                    print(string, attribute101, f"{x} health")
                elif attribute101 == attribute_list[5]:
                    print(string, attribute101, f"{x} amount of absences")
                
            else:
                print("File not loaded, please load a file first.")
            qui = False
            inpu = get_input()
            
                
        elif inpu == commands[5] or inpu == commands[11]:
            print("Program terminated")   
        
        else: 
            print("\nPlease input valid command")
            qui = False
            inpu = get_input()
     
    return
screen(get_input())