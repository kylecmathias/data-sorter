from load_data import check_equal
from load_data import load_data

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
    
list_size_test(load_data('student-mat.csv', "Age"), [82, 104, 98, 82, 24, 3, 1, 1])
list_size_test(load_data('student-mat.csv', "Failures"), [312, 50, 17, 16, 0, 0, 0, 0, 0, 0, 0])
list_size_test(load_data('student-mat.csv', "Health"), [47, 45, 91, 66, 146])
list_size_test(load_data('student-mat.csv', "School"), [79, 80,80, 80, 76])