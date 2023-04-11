from load_data import load_data

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

individual_student_entries_test("student-mat.csv")                                      
