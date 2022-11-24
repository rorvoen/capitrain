from math import inf

from Footprint import footprint
from GeneratedFunctions import pos_max_max_peak
from Testing import testing
from TimeSeriesParser import *
from GenerateFunctions import *
from Enums.Semantics import Semantics


test_sequence = [4, 4, 2, 2, 3, 5, 5, 6, 3, 1, 1, 2, 2, 2, 2, 2, 2, 1]
print(test_sequence)

test_signature = time_series_to_signature_parser(test_sequence)
print(test_signature)

test_semantics = signature_to_semantic(test_signature, Patterns.PEAK)
print(test_semantics)

generate_functions()

pos_max_max_peak(test_sequence)

# testing()

"""test_footprint = footprint(test_semantics)
print(test_footprint)"""

# [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2]
# [4, 4, 2, 2, 3, 5, 5, 6, 3, 1, 1, 2, 2, 2, 2, 2, 2, 1]
# [[3, 5, 5, 6, 3], [2, 2, 2, 2, 2, 2]]
# Feature max/min de chaque tableau/pattern
# [3, 5, 5, 6, 3]
# Aggregateur max/min de

"""for semantic in Semantics:
    write_guard_lines(semantic, "0", "min", "max")"""
