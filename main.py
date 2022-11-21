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