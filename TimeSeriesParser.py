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
    for word in semantics:
        res.append(float(-inf))

    i = 0
    while i < len(semantics):
        match semantics[i]:
            case Semantics.FOUND:
                res[i] = 1
            case Semantics.FOUND_END:
                res[i] = 1
            case Semantics.MAYBE_BEFORE:
                j = i  # On set le compteur de remontée
                # Tant qu'on trouve des maybe on remonte
                while semantics[j] == Semantics.MAYBE_BEFORE:
                    j += 1  # On remonte
                # On a trouvé autre chose que maybe, on regarde si c'est found
                if (semantics[j] == Semantics.FOUND) | (semantics[j] == Semantics.FOUND_END):
                    k = j  # On marque la position du found
                    # On redescend au premier maybe en marquant tous les elements comme dans l'occurence
                    while j >= i:
                        res[j] = 1
                        j -= 1  # On redescend
                    i = k  # On  place i à la position après le found trouvé après les maybe
            case Semantics.OUT_RESET:
                print("")
            case Semantics.IN:
                res[i] = 1
            case Semantics.MAYBE_AFTER:
                j = i  # On set le compteur de remontée
                # Tant qu'on trouve des maybe on remonte
                while semantics[j] == Semantics.MAYBE_AFTER:
                    j += 1  # On remonte
                # On a trouvé autre chose que maybe, on regarde si c'est found
                in_detected = False
                if (semantics[j] == Semantics.IN): in_detected = True
                k = j  # On marque la position du IN
                # On redescend au premier maybe en marquant tous les elements comme dans l'occurence ou non selon la detection
                while j >= i:
                    if in_detected:
                        res[j] = 1
                    j -= 1  # On redescend
                i = k  # On  place i à la position après le found trouvé après les maybe
            case Semantics.OUT_AFTER:
                res[i] = float(-inf)
                res[i-1] = 1
            case Semantics.OUT:
                res[i] = float(-inf)
        print(res)
        i += 1
    return res