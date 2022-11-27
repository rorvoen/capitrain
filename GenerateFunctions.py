import json
import re

from Enums.Patterns import Patterns
from Enums.Semantics import Semantics
from Enums.Aggregators import Aggregators


# This function generates all the possible combinations of aggregators, features and patterns
def generate_functions():
    f = open("GeneratedFunctions.py", "w")
    # Writing imports
    f.write("from math import inf\n")
    f.write("from Enums.Patterns import Patterns\n")
    f.write("from GuardValue import GuardValue\n")
    f.write("from TimeSeriesParser import *\n\n\n")

    # Getting all the tables from Json files
    tables = json.load(open('Json/DecorationTables.json'))["tables"]
    aggregators = tables["aggregators"]
    features = tables["features"]
    decoration = tables["decoration"]
    patterns = json.load(open('Json/Graphs.json'))["graphs"]

    # Iterating on aggregators
    for aggregator in aggregators:
        # Iterating of features
        for feature in features:
            g = aggregator.lower()
            phi_f = features[feature]["phi_f"]
            #Iterating on patterns
            for pattern in Patterns:
                f.write("def pos_" + aggregator.lower() + "_" + feature + "_" + pattern.value + "(time_series):\n")

                # Writing the time_series to signature function call line
                f.write("    signature = time_series_to_signature_parser(time_series)\n")
                # Writing the signature to semantics function call line
                f.write("    semantics = signature_to_semantic(signature, Patterns." + pattern.name + ")\n")

                # Declaring the default_g_f constant
                f.write("    default_g_f = " + float(
                    features[feature][aggregators[aggregator]["default_g_f"]]).__str__() + "\n")
                # Declaring the neutral_f constant
                f.write("    neutral_f = " + float(features[feature]["neutral_f"]).__str__() + "\n")
                f.write("\n")

                # Declaring accumulators
                f.write("    R = default_g_f\n    C = default_g_f\n    D = neutral_f\n\n")

                # Declaring guard tables
                f.write(
                    "    at = [GuardValue(0)]*len(time_series)\n    ct = [GuardValue(0)]*len(time_series)\n    f = [GuardValue(0)]*len(time_series)\n\n")

                # Declaring the i counter for getting current value in the series
                f.write("    i = 0\n\n")

                f.write("    for word in semantics:\n")

                # Declaring delta_f which sometime is equal to current position in time series
                if features[feature]["delta_f"] == "x_i":
                    f.write("        delta_f = time_series[i]\n")
                    f.write("        delta_f_1 = time_series[i+1]\n")
                else:
                    f.write("        delta_f = " + features[feature]["delta_f"] + "\n")

                # Writing the different cases for each semantic word
                f.write("        match word:\n")
                for word in Semantics:
                    after_value = patterns[pattern.value]["after"].__str__()
                    f.write("            case Semantics." + word.name + ":\n")
                    f.write(prepare_guard_lines(word, after_value, g, phi_f, 4) + "\n")
                    operations = decoration["after" + after_value][word.value]
                    for operation in operations:
                        f.write("                " + prepare_operation_line(operation, g, phi_f) + "\n\n")

                f.write("        i += 1 \n\n")

                # Guard end conditions
                f.write("    f[len(time_series) - 1] = GuardValue(0)\n")
                f.write("    if C " + ("<" if aggregator == Aggregators.MIN.value else ">") + " R:\n")
                f.write("        ct[len(time_series) - 1] = GuardValue(1)\n")
                f.write("        at[len(time_series) - 1] = GuardValue(0)\n")
                f.write("    elif (C == R) & (R == default_g_f):\n")
                f.write("        ct[len(time_series) - 1] = GuardValue(0)\n")
                f.write("        at[len(time_series) - 1] = GuardValue(0)\n")
                f.write("    elif (C == R) & (R != default_g_f):\n")
                f.write("        ct[len(time_series) - 1] = GuardValue(1)\n")
                f.write("        at[len(time_series) - 1] = GuardValue(1)\n")
                f.write("    elif R " + ("<" if aggregator == Aggregators.MIN.value else ">") + " C:\n")
                f.write("        ct[len(time_series) - 1] = GuardValue(0)\n")
                f.write("        at[len(time_series) - 1] = GuardValue(1)\n\n")

                # Writing return statement
                f.write("\n    return " + g + "(R,C), time_series, f\n")
                f.write("\n\n")

    f.close()


# Preparation of an operation on an accumulator using the decoration table JSON
def prepare_operation_line(operation, g, phi_f, sub_op=False):
    line = ""
    # Beginning of the code line generated (if not a sub operation)
    if not sub_op:
        line = line + operation["acc"] + " = "

    # Getting the second value, if variable get the name, if other operation preparing it
    value2 = ""
    if "value2" in operation:
        if not (isinstance(operation["value2"], str)):
            value2 = "(" + prepare_operation_line(operation["value2"], g, phi_f, True) + ")"
        else:
            if (value2 == "inf") | (value2 == "-inf"):
                value2 = "float(" + operation["value2"] + ")"
            else:
                value2 = operation["value2"]

    # Getting the first value and the operator
    value1 = ""
    if (value1 == "inf") | (value1 == "-inf"):
        value1 = "float(" + operation["value1"] + ")"
    else:
        value1 = operation["value1"]
    operator = operation["operator"]

    # Finishing line writing
    if operator == "affect":
        line = line + value1
    elif operator == "g":
        operator = g
        line = line + operator + "(" + value1 + ", " + value2 + ")"
    elif operator == "phi_f":
        operator = phi_f
        line = line + operator + "(" + value1 + ", " + value2 + ")"

    return line


# Preparation of the guard operations lines using the decoration table JSON
def prepare_guard_lines(semantic, after_value, g, phi_f, nb_tab):
    lines = ""
    # Defining a variable to indent the code block according to the level it will be writen in the final file
    tab = nb_tab * "    "
    # Getting the appropriate part of the decoration table
    tables = json.load(open('Json/DecorationTables.json'))["tables"]
    guard_table = tables["decoration"]["guard"]["after" + after_value]
    for case in guard_table[semantic.value]:
        condition = "condition" in case
        if condition:
            condition = "if " + case["condition"] + ":"
            if g == "max":
                condition = condition.replace("<g", ">")
            elif g == "min":
                condition = condition.replace("<g", "<")
            condition = condition.replace("phi_f", phi_f)
            lines = lines + tab + condition + "\n"
        for operation in case["operations"]:
            if condition:
                lines = lines + "    "
            var = operation["var"]
            value = operation["value"]
            if isinstance(value, int):
                lines = lines + tab + var + " = GuardValue(" + value.__str__() + ")" + "\n"
            else:
                match = re.search(r"(at|ct|f)\[(i\+1|i)\]", value)
                if not (match is None):
                    lines = lines + tab + var + " = GuardValue(float(inf), " + match.group(1) + ", " + match.group(2) + ", \"" + match.group(1) + "\")" + "\n"
    return lines
