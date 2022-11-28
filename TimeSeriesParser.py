import json
from math import inf

from Enums.Semantics import Semantics

# Providing a time series in input, getting the signature in output
def time_series_to_signature_parser(time_series):
    res = []
    i = 0
    while i < len(time_series) - 1:
        if time_series[i] > time_series[i + 1]:
            res.append(">")
        elif time_series[i] < time_series[i + 1]:
            res.append("<")
        elif time_series[i] == time_series[i + 1]:
            res.append("=")
        i += 1
    return res


# Providing a time series signature in input and the requested pattern
# Getting the corresponding list of semantic words in output
def signature_to_semantic(signature, pattern):
    res = []
    # Loading the graphs from the JSON file
    graph = json.load(open('Json/Graphs.json'))["graphs"][pattern.value]
    # Getting the entry state and setting it as the current one
    current_state = graph["entryState"]
    # Getting all the states and their datas
    states = graph["states"]
    i = 0
    while i < len(signature):  # Iterating on the signature
        transitions = states[current_state]["transitions"]
        j = 0
        # Searching for the right transition according to the current signature symbol
        while j < len(transitions):
            if signature[i] == transitions[j]["consume"]:
                # Adding the produced semantic word to the result list
                res.append(Semantics(transitions[j]["produce"]))
                # Moving to the next state
                current_state = transitions[j]["to"]
                break
            j += 1
        i += 1
    return res
