import json

import GeneratedFunctions


# Testing all the methods using test datas from a JSON file (data from the provided research article)
def testing():
    # Loading the tests
    testing = json.load(open('Json/TestData.json'))["testing"]
    total_ok = 0
    total_ko = 0
    for test in testing:
        function = getattr(GeneratedFunctions, test)  # Getting the function to execute according to the test name
        res = function(testing[test]["time_series"])  # Executing the function with the time series from the test file
        # Checking if test is ok, then updating counters according to the result
        if ((res[0], res[1], res[2]).__str__()) == ((testing[test]["result"], testing[test]["time_series"], testing[test]["found"]).__str__()):
            total_ok += 1
        else:  # If not valid printing the failure details
            total_ko += 1
            print("-------------------------")
            print(test + " is KO")
            print("Result   "+(res[0], res[1], res[2]).__str__())
            print("Expected "+(testing[test]["result"], testing[test]["time_series"], testing[test]["found"]).__str__())
            print("-------------------------")

    # Printing the testing general report
    print("==============================")
    print(total_ok.__str__() + " out of " + len(testing).__str__() + " tests (" + total_ko.__str__() + " KO)")
    print("==============================")
