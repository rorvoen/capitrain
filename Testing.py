import json

import GeneratedFunctions


def testing():
    testing = json.load(open('JeuTest.json'))["testing"]
    total_ok = 0
    total_ko = 0
    for test in testing:
        function = getattr(GeneratedFunctions, test)
        res = function(testing[test]["time_series"])
        print(res)
        print((testing[test]["result"], testing[test]["time_series"], testing[test]["found"]))
        if res == (testing[test]["result"], testing[test]["time_series"], testing[test]["found"]):
            total_ok += 1
        else:
            total_ko += 1
            print("-------------------------")
            print(test + " is KO")
            print("-------------------------")

    print("==============================")
    print(total_ok.__str__() + " out of " + len(testing).__str__() + " tests (" + total_ko.__str__() + " KO)")
    print("==============================")
