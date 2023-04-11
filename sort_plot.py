import string
import matplotlib.pyplot as plt
from load_data import load_data, add_average
import numpy as np
# Function 1 ---------------------------------------------------------------------------------------------------------------


def student_list(data_dictionary: dict) -> list:
    """The function takes one of the loaded dictionaries as an parameter: data_school, data_age,
    data_health, and data_failures and returns a list with all the dictionaries, with the key of the 
    original dictionary and its value added to the end in the order that the original dictionary was in.

    >>>student_list(data_school)
    [{'Age': '18', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6',
        'G3': '6', 'G_avg': 5.67, 'School': 'GP'}, {...}, ...]

    >>>student_list(data_age)
    [{'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10,
        'G_avg': 8.33, 'Age': 15}, {...}, ...]

    >>>student_list(data_health)
    [{'School': 'GP', 'Age': '17', 'StudyTime': '2', 'Failures': '0', 'Absences': '6', 'G1': '6', 'G2': '5',
        'G3': '6', 'G_avg': 5.67, 'Health': 1}, {...}, ...]

    >>>student_list(data_failures)
    [{'School': 'GP', 'Age': '18', 'StudyTime': '2', 'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6',
        'G3': '6', 'G_avg': 5.67, 'Failures': 0}, {...}, ...]
    """
    data_list = []  # Create an empty list that will be filled and returned
    # Create a variable for the header that the dictionary is sorted by
    dictionary_sort = None

    for key in data_dictionary:  # Iterate through each key in the original dictionary
        # Iterate through each dictionary in the list assigned to the key
        for data_set in data_dictionary[key]:
            if 'School' not in data_set:  # Determine which header is missing and assume that that is the type that the list is sorted by
                dictionary_sort = 'School'  # Set the sorting type
            elif 'Age' not in data_set:
                dictionary_sort = 'Age'
            elif 'Health' not in data_set:
                dictionary_sort = 'Health'
            elif 'Failures' not in data_set:
                dictionary_sort = 'Failures'
            """else: #If none of the above headers are missing then assume that the wrong dictionary was used
                print("Wrong dictionary type", data_set)
                exit"""
    temporary_dictionary = {
        dictionary_sort: None}  # Create a temporary dictionary that has the header
    for key_value in data_dictionary:  # Iterate through each key in the original dictionary
        # Iterate through each dictionary in the list assigned to the key
        for data_headers in data_dictionary[key_value]:
            # Overwrite the temporary dictionary to have the key type and value
            temporary_dictionary[dictionary_sort] = key_value
            # Add they key type and value back into the dictionary as another header
            data_headers.update(temporary_dictionary)
            # Add the dictionary to the end of the data list
            data_list.append(data_headers)
    # print(data_list) #Print the data list
    return(data_list)  # Return the data list

#Function 2--------------------------------------------------------------------------------------------------------------------------#


def sort_students_bubble(data_dictionary: dict, attribute: str) -> list:
    """returns a sorted list of the student data by the attribute indicated in the input string and stored as individual dictionaries.

    Preconditions: attributes = Age, Health, StudyTime, G_Avg, School, Absences, G1, G2, G3
    """
    sorted_list = student_list(data_dictionary)
    swap = True
    while swap:
        swap = False
        for i in range(len(sorted_list) - 1):
            if sorted_list[i].get(attribute) > sorted_list[i + 1].get(attribute):

                sorted_list[i], sorted_list[i +
                                            1] = sorted_list[i + 1], sorted_list[i]
                swap = True

    return sorted_list
#Function 3--------------------------------------------------------------------------------------------------------------------------#


def sort_students_selections(student_data: dict, attribute: str) -> dict:
    """returns a sorted list with student sata stored as individual dictionaries

    Preconditions: attributes = Age, Health, StudyTime, G_Avg, School, Absences, G1, G2, G3

    >>>sort_students_selections(load_data("student-mat.csv", "Health"), "G1")
    {'School': 'GP', 'Age': '17', 'StudyTime': '2', 'Failures': '0', 'Absences': '6', 'G1': '6', 'G2': '5', 'G3': '6', 'Health': 1}... 
    None
    >>>sort_students_selections(load_data("student-mat.csv", "Age"), "G1")
    {'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'Age': 15}...
    None
    >>>sort_students_selections(load_data("student-mat.csv", "School"), "G2")
    {'Age': '18', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6', 'School': 'GP'}...
    None
    """
    students = student_list(student_data)

    for i in range(len(students)):
        min_index = i
        for u in range(i + 1, len(students)):
            if students[min_index][attribute] > students[u][attribute]:
                min_index = u
            students[i], students[min_index] = students[min_index], students[i]
#Function 4--------------------------------------------------------------------------------------------------------------------------#


def curve_fit(generated_dictionary: dict, attribute: str, degree_of_polynomial: int) -> list:
    """The function takes one of the dictionaries from the load_data module, one 
    of the categories that has integers assigned to it (like Health but not school)
    and an integer to represent the degree of the polynomial. The function returns 
    a list of numbers to represent the coefficients assigned to the standard form
    of the polynomial of best fit. The function assumes that the exact variables
    with the assigned dictionaries are loaded, the attributes have the first
    letter capitalized and the rest lowercase, and the degree of polynomial is 
    an integer between 1 and 5 inclusive.
    >>>curve_fit(data_age, 'Health', 3)
    [-0.01814103,  0.42884615, -2.79955128, 11.02884615]
    >>>curve_fit(data_school, 'Failures', 4)
    [-0.01814103,  0.42884615, -2.79955128, 11.02884615]
    >>>curve_fit(data_failures, 'Age', 4)
    [-1.94643164e-02,  1.35658729e+00, -3.51888980e+01,  4.02459068e+02,
       -1.70141865e+03]
    """
    attribute_averages = {}
    average_total = {}
    average_divider = {}
    x_values = []
    y_values = []
    data_list = student_list(generated_dictionary)
    for data_set in data_list:
        average_total[int(data_set[attribute])] = 0
        average_divider[int(data_set[attribute])] = 0

    for data_set2 in data_list:
        average_total[int(data_set2[attribute])] += int(data_set2['G_avg'])
        average_divider[int(data_set2[attribute])] += 1

    for averages in average_total:
        attribute_averages[averages] = (
            average_total[averages] / average_divider[averages])

    index_count = 0

    for unsorted in attribute_averages:
        y_values.append(unsorted)

    for y in y_values:
        y_values[index_count] = int(y)
        index_count += 1
    temp_y_values = y_values
    y_values = []

    for i in range(len(temp_y_values)):
        smallest = min(temp_y_values)
        temp_y_values.pop(temp_y_values.index(smallest))
        y_values.append(smallest)
    for x in y_values:
        x_values.append(attribute_averages[x])

    tempx = y_values
    y_values = x_values
    x_values = tempx

    if len(y_values) - 1 < degree_of_polynomial:
        return np.polyfit(x_values, y_values, len(y_values) - 1), [min(x_values), max(x_values)]
    else:
        return np.polyfit(x_values, y_values, degree_of_polynomial), [min(x_values), max(x_values)]
#Function 5--------------------------------------------------------------------------------------------------------------------------#


def histogram(student_dict: dict, attribute: str) -> None:
    """Takes a dictionary from load date, an atttribute like "Age". Plots a histogram based
    on the attribute and dictionary. Returns None
    Precodition: attributes must be either "Age", "Health", "School", Or "Failures"

    >>> histogram(load_data("", 'School'), 'School')
    >>> histogram(load_data("", 'Age'), 'School')
    """
    number_students_per_att = {}
    temp_dic = {}
    x_label = None

    if attribute == "Age":
        x_label = "Ages"
    elif attribute == "School":
        x_label = "Schools"
    elif attribute == "Health":
        x_label = "Healths"
    elif attribute == "Failures":
        x_label = "Failures"

    student_lis = student_list(student_dict)
    for i in student_lis:
        temp_dic.update({i[attribute]: ""})
    x_axis = sorted(temp_dic)

    count = 0
    for key in x_axis:
        for j in student_lis:
            if key == j[attribute]:
                count += 1
        number_students_per_att.update({key: count})
        count = 0

    y_axis = []
    for i in number_students_per_att.values():
        y_axis.append(i)

    plt.bar(x_axis, y_axis, width=0.4, linewidth=20, color="teal")
    plt.xlabel(x_label)
    plt.ylabel("Number of students")
    plt.title(F"The Amount of students for each {attribute}")
    plt.show()


#Tests --------------------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    # Student_list
    data_school = add_average(load_data('student-mat.csv', 'School'))
    data_age = add_average(load_data('student-mat.csv', 'Age'))
    data_health = add_average(load_data('student-mat.csv', 'Health'))
    data_failures = add_average(load_data('student-mat.csv', 'Failures'))
    print(data_age, data_failures, data_school, data_health)
#Histogram Tests ---------------------------------------------------------------------------------------------------------------#
    labels = ["Age", "Health", "School", "Failures"]
    for i in labels:
        tester = add_average(load_data("student-mat.csv", i))
        x = histogram(tester, "G1")
        print(x)

    for i in labels:
        tester = add_average(load_data("student-mat.csv", i))
        x = histogram(tester, "School")
        print(x)

    for i in labels:
        tester = add_average(load_data("student-mat.csv", i))
        x = histogram(tester, "Health")
        print(x)

    for i in labels:
        tester = add_average(load_data("student-mat.csv", i))
        x = histogram(tester, "Failures")
        print(x)
        
# Curve fitting tests
    categories = ['Health', 'Age', 'Failures',
                  'StudyTime', 'Absences', 'G1', 'G2', 'G3']
    for poly_iteration in range(1, 6):
        for category_test in categories:
            print(curve_fit(data_age, category_test,
                  poly_iteration), 'age', category_test)
            print(curve_fit(data_school, category_test,
                  poly_iteration), 'school', category_test)
            print(curve_fit(data_health, category_test,
                  poly_iteration), 'health', category_test)
            print(curve_fit(data_failures, category_test,
                  poly_iteration), 'failures', category_test)


def main():
    print(student_list(data_school))
    print('--------------------------------------------------------')
    print(sort_students_bubble(data_school, 'Age'))
    print('--------------------------------------------------------')
    print(sort_students_selections(data_school, 'Age'))
    print('--------------------------------------------------------')
    print(curve_fit(data_school, 'Age', 3))
    print('--------------------------------------------------------')
    print(histogram(data_school, 'Age'))


if __name__ == "__main__":
    main()
