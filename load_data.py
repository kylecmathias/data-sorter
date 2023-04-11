import string
from typing import List


def student_age_dictionary(file: str) -> dict:
    """Takes an csv file with specific headings and returns an organized dictionary where the keys are students age
    and the values are the students with those ages. 
    
    Precondition: the header in the given file must include "Age", "School", "StudyTime", "Failures", "Health", "Absences", 
    "G1", "G2", "G3" *they dont have to be the same order line 39 - 47 sloved that
    
    print(student_age_dictionary('student-mat.csv')) 
    
    
        { 15 : [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3, 'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10},
            {another element}, … ],
          16 : [ {'School': 'MS', 'StudyTime': 1, 'Failures': 1.2, 'Health': 4, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7},
                {another element}, … etc]

    
    """
    FILE = open(file, 'r')
    LINE = FILE.readlines()
    UNEDITED_TEXT = [LINE]
    FILE.close()

    student_age_dictionary = {}

    lis_students = []
    for i in UNEDITED_TEXT: #organizes file in more readable way
        for j in i:
            temp = j.strip()
            temp = temp.split(',')
            lis_students.append(temp)
    header = lis_students[0] #saves the header to its own thing
    lis_students.pop(0)

    age = header.index("Age") #pointless process of finding the indexes for headers
    school = header.index("School")
    studytime = header.index("StudyTime")
    fail = header.index("Failures")
    health = header.index("Health")
    absences = header.index("Absences")
    g1 = header.index("G1")
    g2 = header.index("G2")
    g3 = header.index("G3")
    age_dic = {}

    for i in lis_students: #reads over data
        i[age] = int(i[age]) #for this line to ine 61, changes all the numbers to intergers.
        i[studytime] = int(i[studytime])
        i[fail] = int(i[fail])
        i[health] = int(i[fail])
        i[absences] = int(i[absences])
        i[g1] = int(i[g1])
        i[g2] = int(i[g2])
        i[g3] = int(i[g3])
        age_dic.update({i[age]: []})
        keys = sorted(age_dic) #makes a sorted key

    for i in range(len(keys)): #changes keys to ints and adds keys to the main  dictionary
        keys[i] = int(keys[i])
        student_age_dictionary.update({keys[i]: []})

    lis = []
    lis2 = []
    for i in keys: # sorts the data into order by age
        for j in lis_students:
            if i == j[age]:
                lis.append(j)

    counter = keys[0]
    for i in lis: #this makes the final dicitonary,
        if i[age] == counter + 1: #this is to check when it changes age
            counter += 1
            lis2 = []
        #this makes a temp list with all the current ages in it
        lis2.append({header[school]: i[school], header[studytime]: i[studytime], header[fail]: i[fail],
                     header[health]: i[health], header[absences]: i[absences], header[g1]: i[g1], header[g2]: i[g2], header[g3]: i[g3]})
        student_age_dictionary.update({counter: lis2}) #adds the temp list to the right place

    #for key in student_age_dictionary:   #this was for easily reading the data.
     #   x = print(f"{key} : {student_age_dictionary[key]}\n")

    return student_age_dictionary


def student_failures_dictionary(file_name: str) -> dict:
    """Returns a dictionary of file_name with the key of number of failures the students have had.
    
    Preconditions: 0 =< failures =< 10
    
    >>> 0 : [{'School': 'GP', 'Age': '18', 'StudyTime': '2', 'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}
    >>> 1 : [{'School': 'GP', 'Age': '16', 'StudyTime': '2', 'Health': '3', 'Absences': '25', 'G1': '7', 'G2': '10', 'G3': '11'}
    >>> 2 : [{'School': 'GP', 'Age': '16', 'StudyTime': '1', 'Health': '5', 'Absences': '14', 'G1': '6', 'G2': '9', 'G3': '8'}
    """
    data = open(file_name, "r")
    data_opened = data.read()
    lines = [] #data within file's lines
    student_data = {} #dict containing sorted student_data
    students = [] #list containing all individual student data
    student = {} #dict containing 1 student data at a time
    student_fails = {}
    #header = data.readline().strip().strip("\n").split(".")
    data_read = data_opened.split()
    header_dict = {}
    data.close()

    for data_splitted in data_read:
        splitted_data = data_splitted.split(",")
        lines.append(splitted_data)

    header = lines[0]
    lines.pop(0)

    for title in header:
        header_dict[title] = str(title)

    for lists in lines:
        student[lists[3]] = lists
        keys = sorted(student)
    #print(keys)

    for i in range(len(keys)):
        keys[i] = int(keys[i])
        student_fails.update({keys[i]: []})
    for i in lines:
        i[3] = int(i[3])
    lis = []
    for i in keys:
        for j in lines:
            if i == j[3]:
                lis.append(j)

    counter = 0
    temp_lis = []
    for i in lis:

        if i[3] == counter + 1:
            counter += 1
            temp_lis = []
        temp_lis.append({"School": i[0], "Age": i[1], "StudyTime": i[2],
                         "Health": i[4], "Absences": i[5], "G1": i[6], "G2": i[7],
                         "G3": i[8]})
        student_fails.update({counter: temp_lis})

    return student_fails


def student_school_dictionary(school_data_file: str) -> dict: #defining the function and its parameters
    opened_school_data = open(school_data_file, 'r') #opens the file
    temporary_school_data = opened_school_data.read() #saves the data in the file to a variable as a string
    opened_school_data.close()

    school_data_values = [] #creates the list for the organized data list
    separate_list = [] # creates the list for the separated lists
    headers = [] #creates the list that will store the headers
    school_initials = [] #creates the list for the initials of each school

    temporary_school_dictionary = {} #creates a temporary dictionary that will store values to be organized
    school_dictionary = {} #creates the final dictionary that will be returned

    separate_list = temporary_school_data.split() #splits the list into mutliple strings at each new line

    for data_list in separate_list: #iterates through each new string
        data_values = data_list.split(',') #changes the string to a list, separated by ','
        school_data_values.append(data_values) #saves each list to a list

    for header in school_data_values[0]: #iterates through each value in the first list
        headers.append(header) #saves the headers to a separate list
        temporary_school_dictionary[header] = None #saves the headers as keys in a dictionary and sets the value of each key to None

    temporary_school_dictionary.pop(headers[0]) #removes the "school" from the header
    headers.pop(0) #removes the school from the list of headers

    school_data_values.pop(0) #removes the headers from the list of lists

    for lists in school_data_values: #iterates through each list in the larger list
        initials = lists[0] #saves the school initials of the current list as a variable
        if school_initials.count(lists[0]) == 0: #determines if the list called 'school initials' doesn't already have the school initials of the current list
            school_initials.append(lists[0]) #adds the school initials to the list
            school_dictionary[lists[0]] = [] #adds the school initials as keys to a dictionary, with the value being an empty list
        temp_school_dictionary = lists #saves the current list
        lists.pop(0) #removes the school initials from the list
        index = 0 #sets the index of each value in the header list
        for values in temp_school_dictionary: #iterates through each value in the list of values
            temp_dict = temporary_school_dictionary #sets a variable with the headers
            temp_dict[headers[index]] = values #adds values to the headers
            index += 1 #changes the index of the next value
        school_dictionary[initials].append(temp_dict.copy()) #adds the dictionary to the list inside the larger dictionary

    return(school_dictionary) #returns the dictionary


def student_health_dictionary(file_name: str) -> dict:
    """Returns a dictionary of file_name with the key displaying their health, ranging from a value pf 1 to 5.

    Preconditions: 0 =< health =< 5

    >>> 0 : [{'School': 'GP', 'Age': '18', 'StudyTime': '2', 'Failures: '0', 'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}
    >>> 1 : [{'School': 'GP', 'Age': '16', 'StudyTime': '2', 'Failures': '0', 'Absences': '25', 'G1': '7', 'G2': '10', 'G3': '11'}
    >>> 2 : [{'School': 'GP', 'Age': '16', 'StudyTime': '1', 'Failures': '3', 'Absences': '14', 'G1': '6', 'G2': '9', 'G3': '8'}
    """
    data = open(file_name, "r")
    data_opened = data.read()
    lines = []  # data within file's lines

    student = {}  # dict containing 1 student data at a time
    student_health = {}
    #header = data.readline().strip().strip("\n").split(".")
    data_read = data_opened.split()
    header_dict = {}
    data.close()

    for data_splitted in data_read:
        splitted_data = data_splitted.split(",")
        lines.append(splitted_data)

    header = lines[0]
    lines.pop(0)

    for title in header:
        header_dict[title] = str(title)

    for lists in lines:
        student[lists[4]] = lists
        keys = sorted(student)
    # print(keys)

    for i in range(len(keys)):
        keys[i] = int(keys[i])
        student_health.update({keys[i]: []})
    for i in lines:
        i[4] = int(i[4])
    lis = []
    for i in keys:
        for j in lines:
            if i == j[4]:
                lis.append(j)

    counter = 0
    temp_lis = []
    for i in lis:

        if i[4] == counter + 1:
            counter += 1
            temp_lis = []
        temp_lis.append({"School": i[0], "Age": i[1], "StudyTime": i[2],
                         "Failures": i[3], "Absences": i[5], "G1": i[6], "G2": i[7],
                         "G3": i[8]})
        student_health.update({counter: temp_lis})

    return student_health


def load_data(file: str, key: str) -> dict:
    """
Returns a dictionary of file_name based off of the desired information by the user.

>>>'GP' : [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,
 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67 },
 {another element},
 … ],
>>>'MB' : [ {'Age': 16, 'StudyTime': 2.6, 'Failures': 0, 'Health': 3,
 'Absences': 12, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33 },
 {another element},
 … ],
 """
    student_dictionary = {}
    if key == "School":
        student_dictionary = student_school_dictionary(file)
    elif key == "Age":
        student_dictionary = student_age_dictionary(file)
    elif key == "Failures":
        student_dictionary = student_failures_dictionary(file)
    elif key == "Health":
        student_dictionary = student_health_dictionary(file)
    else:
        return "Invalid Key"

    return student_dictionary


def add_average(student_dictionary: dict) -> dict:
    """
    The function takes the output of the load data function, which is a dictionary, and 
    returns a nearly identical dictionary, but with a new key at the end of each 
    sub-dictionary, which contains the average of grades 1,2 and 3.
    
    >>>add_average(load_data('student-mat.csv', "Age"))
    {15: [{'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3, 
              'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_avg': 8.33}, {...}
              ...]}
    """
    dictionary = student_dictionary
    avg = 0
    for i in dictionary.values():
        for j in i:
            avg = round((int(j["G1"]) + int(j["G2"]) + int(j["G3"])) / 3, 2)
            j.update({"G_avg": avg})

    return dictionary

