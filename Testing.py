import json

import GeneratedFunctions


def testing():
    testing = json.load(open('JeuTest.json'))["testing"]
    total_ok = 0
    total_ko = 0
    for test in testing:
        function = getattr(GeneratedFunctions, test)
        res = function(testing[test]["time_series"])
        if ((res[0], res[1], res[2]).__str__()) == ((testing[test]["result"], testing[test]["time_series"], testing[test]["found"]).__str__()):
            total_ok += 1
        else:
            total_ko += 1
            print("-------------------------")
            print(test + " is KO")
            print("Result "+(res[0], res[1], res[2]).__str__())
            print("Expected "+(testing[test]["result"], testing[test]["time_series"], testing[test]["found"]).__str__())
            print("-------------------------")

    print("==============================")
    print(total_ok.__str__() + " out of " + len(testing).__str__() + " tests (" + total_ko.__str__() + " KO)")
    print("==============================")
