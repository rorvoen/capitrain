import json

import GeneratedFunctions


def testing():
    tests = json.load(open('JeuTest.json'))["tests"]
    total_ok = 0
    total_ko = 0
    for test in tests:
        function = getattr(GeneratedFunctions, "pos_"+test)
        res = function(tests[test]["data"])
        if res == tests[test]["result"]:
            total_ok += 1
        else:
            total_ko += 1
            print("-------------------------")
            print(test + " is KO")
            print("-------------------------")

    print("==============================")
    print(total_ok.__str__() + " out of " + len(tests).__str__() + " tests (" + total_ko.__str__() + " KO)")
    print("==============================")
