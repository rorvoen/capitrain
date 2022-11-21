import json
from math import inf

from Enums.Semantics import Semantics


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


def signature_to_semantic(signature, pattern):
    res = []
    graph = json.load(open('SignatureToSemanticPatternGraphs.json'))["graphs"][pattern.value]
    current_state = graph["entryState"]
    states = graph["states"]
    i = 0
    while i < len(signature):
        transitions = states[current_state]["transitions"]
        j = 0
        while j < len(transitions):
            if signature[i] == transitions[j]["consume"]:
                res.append(Semantics(transitions[j]["produce"]))
                current_state = transitions[j]["to"]
                break
            j += 1
        i += 1
    return res

def find_pattern_occurrences_semantics(semantics):
    res = []
    for semantic in semantics:
        res.append(float(-inf))




def format_semantics_result(semantics):
    res = "["
    i = 0
    while i < len(semantics):
        if i == len(semantics) - 1:
            res = res + semantics[i].name + "] "
        else:
            res = res + semantics[i].name + ", "
        i += 1
    return res
