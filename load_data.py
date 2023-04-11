import string
from typing import List 


def student_age_dictionary(file: str) -> dict:
    """Takes an csv file with specific headings and returns an organized dictionary where the keys are students age
    and the values are the students with those ages. 
    
    Precondition: the header in the given file must include "Age", "School", "StudyTime", "Failures", "Health", "Absences", 
    "G1", "G2", "G3" *they dont have to be the same order
    
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

def check_equal(description: str, actual, expected) -> int:
    """
    Print a "passed" message if actual and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    actual.
    
    Parameters "actual" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    actual_type = type(actual)
    expected_type = type(expected) 
    if actual != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, actual))
        return 0
    else:
        print("{0} PASSED".format(description))
        return 1
    print("------")

def add_average_test(file: str)-> None:
    """This testing file checks for if the amount of dictionaries in load_data == the amount in add_average,
    if they all have the G_avg, and if theyre right. Returns if all tests passed
    
    >>>testing_add_avg
    
    Test 1: Age Passed, Expected: 395 found: 395
    Test 2: Age Passed, Expected: 'G_avg' 395 times found: 'G_avg' 395 times
    Test 3: Age Passed all the avg's are correct
    ...
    
    
    """
    
    print("Add Average Test:")
    KEY_LIST = ["Age", "School", "Health", "Failures"]
    for key in KEY_LIST:
        dictionary_age = load_data(file, key)
        add_average_ = add_average(dictionary_age)
        temp_lis = []
        counter_key = 0
        counter_main = 0 
        counter = 0
        counter2 = 0 
    
        for list in dictionary_age.values(): #gets how many dictionarys there are in the load_data function; before add avg
            for dict in list:
                counter_main += 1
            
    
        for list in add_average_.values(): #iterates over the add_average_ values to use them for testing
            for dict in list: 
                g_avg = dict.get("G_avg")
                g1 = dict.get('G1')
                g2 = dict.get('G2')
                g3 = dict.get('G3')
                temp_lis.append([int(g1), int(g2), int(g3), g_avg])
                for key2 in dict.keys():
                    if key2 == "G_avg":
                        counter += 1
                counter_key += 1
            
        for list in temp_lis: #checks if "G_avg" is right
            expected_avg = (list[0] + list[1] + list[2]) / 3 
            if abs(expected_avg -  list[3]) <= 0.01: 
                check = True
            else:
                check = False
                
            if check == True:  
                counter2 += 1
    
        if counter_main == counter_key: #test 1
            print("Test 1:", key, "Passed, Expected:", counter_main, "found:", counter_key)
        else:
            print(key, "Test 1: Failed")
        if counter == counter_key: #test 2 
            print("Test 2:", key, "Passed, Expected: 'G_avg'", counter_key,"times" ,"found: 'G_avg'", counter, "times")
        else:
            print(key, "Test 2: Failed")
        if counter2 == counter_key: #test 3 
            print("Test 3:", key, "Passed all the avg's are correct\n")
        else:
            print(key, "Test 3: Failed")
    return 


def list_size_test(student_data: dict, expected: list):
    """Tests all dictionaries in load_data whether or not sum of each key 
    contains the correct amount of entries.
    
    >>>student_data[15] PASSED
    ------
    >>>Total Tests: 8. Tests Passed: 8. Tests Failed: 0
    ------
    >>>student_data[0] PASSED
    ------
    >>>Total Tests: 11. Tests Passed: 11. Tests Failed: 0
    ------
    >>>student_data[2] PASSED
    ------
    >>>Total Tests: 5. Tests Passed: 5. Tests Failed: 0
    """

    print("List Size Test:")
    passed_tests = 0
    total_tests = 0
    failed_tests = 0
   
    i = 0
    for item in student_data:
        total_tests += 1
        if check_equal('student_data{0}'.format('[' + str(item) + ']'), len(student_data[item]), expected[i]) == 0:
            failed_tests += 1
        elif check_equal('student_data{0}'.format('[' + str(item) + ']'), len(student_data[item]), expected[i]) == 1:
            passed_tests += 1
        i += 1
        
    failed_tests =  total_tests - passed_tests
    
    print("Total Tests: {0}. Tests Passed: {1}. Tests Failed: {2}".format(total_tests, passed_tests, failed_tests))


def check_keys(file_name: dict, keys: list) -> dict:
    """
    checks if the keys from each dictionary in the file T123_M1_load_data are correct
    """

    print("Check Keys Test:")
    lists = []
    counter = 0
    for key, value in file_name.items():
        lists.append(key in keys)
        counter += 1
    print(lists, counter)  # prints lists stating if each key is True or False

def individual_student_entries_test(file_name: str) -> None: #Defines the function to take a string parameter and return nothing
    """
    This test determines whether the correct header values appear in each organized set, and 
    prints passed if the test completes successfully. If the test is not completed successfully 
    because there was a missing header in one of the data sets, it will display the value and 
    key of the dictionary that had the error. It will also display all the errors after
    each test is completed and say whether the test was completed successfully or not.
    >>>individual_student_entries_test("student-mat.csv")
    school passed
    errors: None
    age passed
    errors: None
    health passed
    errors: None
    failures passed
    errors: None
    """

    print("Individual Student Entries Test:")
    loaded_student_school_dictionary = load_data(file_name, "School") #Loads the data as organized by each header into dictionaries 
    loaded_student_age_dictionary = load_data(file_name, "Age")
    loaded_student_health_dictionary = load_data(file_name, "Health")
    loaded_student_failures_dictionary = load_data(file_name, "Failures")

    school_indexes = ["Age", "StudyTime", "Failures", "Health", "Absences", "G1", "G2", "G3"] #Assigns all possible headers for the dictionary to a list 

    school_pass = "passed" #Sets the default test result to pass
    school_error = None #Sets the error to none

    for school_dictionary in loaded_student_school_dictionary: #Iterates through each school in the dictionary
        for data_organized_by_school in loaded_student_school_dictionary[school_dictionary]: #Iterates through each dictionary assigned to each school
            for school_organized in data_organized_by_school: #Iterates through each header in each dictionary
                if school_organized not in school_indexes: #If the header is not in the previously defined list
                    print(loaded_student_school_dictionary[school_dictionary], "failed") #Print the dictionary that failed the test
                    print(school_organized, "not in", school_indexes) #Print that the header is not in the dictionary
                    school_pass = "failed" #Set the overall test score to fail
                    school_error = loaded_student_school_dictionary[school_dictionary] #Set the dictionary that has the error to a variable
                    break
    print("school", school_pass) #Print whether the school test was passed
    print("errors:", school_error) #Print the last error that occured

    age_indexes = ["School", "StudyTime", "Failures", "Health", "Absences", "G1", "G2", "G3"] #Assigns all possible headers for the dictionary to a list 

    age_pass = "passed" #Sets the default test result to pass
    age_error = None #Sets the error to none

    for age_dictionary in loaded_student_age_dictionary: #Iterates through each age in the dictionary
        for data_organized_by_age in loaded_student_age_dictionary[age_dictionary]: #Iterates through each dictionary assigned to each age
            for age_organized in data_organized_by_age: #Iterates through each header in each dictionary
                if age_organized not in age_indexes: #If the header is not in the previously defined list
                    print(loaded_student_age_dictionary[age_dictionary], "failed") #Print the dictionary that failed the test
                    print(age_organized, "not in", age_indexes) #Print that the header is not in the dictionary
                    age_pass = "failed" #Set the overall test score to fail
                    age_error = loaded_student_age_dictionary[age_dictionary] #Set the dictionary that has the error to a variable
                    break
    print("age", age_pass) #Print whether the age test was passed
    print("errors:", age_error) #Print the last error that occured

    health_indexes = ["School", "Age", "StudyTime", "Failures", "Absences", "G1", "G2", "G3"] #Assigns all possible headers for the dictionary to a list 

    health_pass = "passed" #Sets the default test result to pass
    health_error = None #Sets the error to none

    for health_dictionary in loaded_student_health_dictionary: #Iterates through each health in the dictionary
        for data_organized_by_health in loaded_student_health_dictionary[health_dictionary]: #Iterates through each dictionary assigned to each health
            for health_organized in data_organized_by_health: #Iterates through each header in each dictionary
                if health_organized not in health_indexes: #If the header is not in the previously defined list
                    print(loaded_student_health_dictionary[health_dictionary], "failed") #Print the dictionary that failed the test
                    print(health_organized, "not in", health_indexes) #Print that the header is not in the dictionary
                    health_pass = "failed" #Set the overall test score to fail
                    health_error = loaded_student_health_dictionary[health_dictionary] #Set the dictionary that has the error to a variable
                    break
    print("health", health_pass) #Print whether the health test was passed
    print("errors:", health_error) #Print the last error that occured

    failures_indexes = ["School", "Age", "StudyTime", "Health", "Absences", "G1", "G2", "G3"] #Assigns all possible headers for the dictionary to a list 

    failures_pass = "passed" #Sets the default test result to pass
    failures_error = None #Sets the error to none

    for failures_dictionary in loaded_student_failures_dictionary: #Iterates through each failures in the dictionary
        for data_organized_by_failures in loaded_student_failures_dictionary[failures_dictionary]: #Iterates through each dictionary assigned to each failure
            for failures_organized in data_organized_by_failures: #Iterates through each header in each dictionary
                if failures_organized not in failures_indexes: #If the header is not in the previously defined list
                    print(loaded_student_failures_dictionary[failures_dictionary], "failed") #Print the dictionary that failed the test
                    print(failures_organized, "not in", failures_indexes) #Print that the header is not in the dictionary
                    failures_pass = "failed" #Set the overall test score to fail
                    failures_error = loaded_student_failures_dictionary[failures_dictionary] #Set the dictionary that has the error to a variable
                    break
    print("failures", failures_pass) #Print whether the failures test was passed
    print("errors:", failures_error) #Print the last error that occured


def main():
    
    add_average_test("student-mat.csv")

    print("-------------------------------------------")
    list_size_test(load_data('student-mat.csv', "Age"), [82, 104, 98, 82, 24, 3, 1, 1])
    list_size_test(load_data('student-mat.csv', "Failures"), [312, 50, 17, 16, 0, 0, 0, 0, 0, 0, 0])
    list_size_test(load_data('student-mat.csv', "Health"), [47, 45, 91, 66, 146])
    list_size_test(load_data('student-mat.csv', "School"), [79, 80,80, 80, 76])

    print("-------------------------------------------")
    dict_age = student_age_dictionary('student-mat.csv')
    # checks the keys in student_age_dictionary
    check_keys(dict_age, [15, 16, 17, 18, 19, 20, 21, 22])

    dict_failures = student_failures_dictionary('student-mat.csv')
    # checks the keys in student_failures_dictionary
    check_keys(dict_failures, [0, 1, 2, 3])

    dict_school = student_school_dictionary('student-mat.csv')
    # checks the keys in student_school_dictionary
    check_keys(dict_school, ['GP', 'MB', 'CF', 'BD', 'MS'])

    dict_health = student_health_dictionary('student-mat.csv')
    # checks the keys in student_health_dictionary
    check_keys(dict_health, [1, 2, 3, 4, 5])

    print("-------------------------------------------")
    individual_student_entries_test("student-mat.csv")                                      

if __name__ == "__main__":
    main()
# end main