import json

from Enums.Patterns import Patterns
from Enums.Semantics import Semantics


def generate_functions():
    f = open("GeneratedFunctions.py", "w")
    f.write("from math import inf\n")
    f.write("from Enums.Patterns import Patterns\n")
    f.write("from TimeSeriesParser import *\n\n\n")
    f.close()

    tables = json.load(open('DecorationTables.json'))["tables"]
    aggregators = tables["aggregators"]
    features = tables["features"]
    decoration = tables["decoration"]
    patterns = json.load(open('SignatureToSemanticPatternGraphs.json'))["graphs"]

    f = open("GeneratedFunctions.py", "a")
    for aggregator in aggregators:
        for feature in features:
            g = aggregator.lower()
            phi_f = features[feature]["phi_f"]
            for pattern in Patterns:
                f.write("def pos_" + aggregator.lower() + "_" + feature + "_" + pattern.value + "(time_series):\n")

                # Writing the time_series to signature function call line
                f.write("    signature = time_series_to_signature_parser(time_series)\n")
                # Writing the signature to semantics function call line
                f.write("    semantics = signature_to_semantic(signature, Patterns." + pattern.name + ")\n")

                # Declaring the default_g_f constant
                f.write("    default_g_f = " + float(features[feature][aggregators[aggregator]["default_g_f"]]).__str__() + "\n")
                # Declaring the neutral_f constant
                f.write("    neutral_f = " + float(features[feature]["neutral_f"]).__str__() + "\n")
                f.write("\n")

                # Declaring accumulators
                f.write("    R = default_g_f\n    C = default_g_f\n    D = neutral_f\n\n")

                # Declaring the i counter for getting current value in the series
                f.write("    i = 0\n\n")

                f.write("    for word in semantics:\n")

                # Declaring delta_f which sometime is equal to current position in time series
                if features[feature]["delta_f"] == "x_i":
                    f.write("        delta_f = time_series[i]\n")
                else:
                    f.write("        delta_f = " + features[feature]["delta_f"] + "\n")

                f.write("        match word:\n")
                for word in Semantics:
                    if bool(decoration[word.value]):  # Checking if there is operations for this word
                        f.write("            case Semantics." + word.name + ":\n")
                    operations = decoration[word.value]
                    for operation in operations:
                        f.write("                " + prepare_operation_line(operation, g, phi_f) + "\n")

                f.write("        i += 1 \n")

                f.write("\n    return " + g + "(R, C)\n")
                f.write("\n\n")

    f.close()


def prepare_operation_line(operation, g, phi_f, sub_op = False):
    line = ""
    # Beginning of the code line generated (if not a sub operation
    if not sub_op:
        line = line + operation["acc"] + " = "

    # Getting the second value, if variable get the name, if other operation preparing it
    value2 = ""
    if "value2" in operation:
        if not (isinstance(operation["value2"], str)):
            value2 = "(" + prepare_operation_line(operation["value2"], g, phi_f, True) + ")"
        else:
            value2 = "float(" + operation["value2"] + ")"

    # Getting the first value and the operator
    value1 = "float(" + operation["value1"] + ")"
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
