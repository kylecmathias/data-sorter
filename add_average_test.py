from load_data import load_data
from load_data import add_average

def add_average_test(file: str)-> None:
    """This testing file checks for if the amount of dictionaries in load_date == the amount in add_average,
    if they all have the G_avg, and if theyre right. Returns if all tests passed
    
    >>>testing_add_avg
    
    Test 1: Age Passed, Expected: 395 found: 395
    Test 2: Age Passed, Expected: 'G_avg' 395 times found: 'G_avg' 395 times
    Test 3: Age Passed all the avg's are correct
    ...
    
    
    """
    
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
            

print(add_average_test("student-mat.csv"))