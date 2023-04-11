import string
from load_data import student_age_dictionary, student_failures_dictionary, student_school_dictionary, student_health_dictionary


def check_keys(file_name: dict, keys: list) -> dict:
    """
    checks if the keys from each dictionary in the file load_data are correct
    """
    lists = []
    counter = 0
    for key, value in file_name.items():
        lists.append(key in keys)
        counter += 1
    print(lists, counter)  # prints lists stating if each key is True or False


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


