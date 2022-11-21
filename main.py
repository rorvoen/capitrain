from math import inf

from Testing import testing
from TimeSeriesParser import *
from GenerateFunctions import *

test_sequence = [4, 4, 2, 2, 3, 5, 5, 6, 3, 1, 1, 2, 2, 2, 2, 2, 2, 1]
print(test_sequence)

test_signature = time_series_to_signature_parser(test_sequence)
print(test_signature)

test_semantics = signature_to_semantic(test_signature, Patterns.PEAK)
print(format_semantics_result(test_semantics))

generate_functions()

testing()


def pos_max_max_increasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING)
    print(format_semantics_result(semantics))
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        print(delta_f)
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))
                D = float(neutral_f)
            case Semantics.FOUND_END:
                R = max(float(R,), (max(float(D), float(delta_f))))
                D = float(neutral_f)
            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))
            case Semantics.OUT_RESET:
                D = float(neutral_f)
            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))
                D = float(neutral_f)
            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))
            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))
                C = float(default_g_f)
                D = float(neutral_f)
        i += 1

    return max(R, C)


# print(pos_max_max_increasing([4,3,5,5,2,1,1,3,3,4,6,6,3,1,3,3]))


