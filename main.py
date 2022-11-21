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

test_semantics2 = [Semantics.OUT, Semantics.OUT, Semantics.MAYBE_BEFORE, Semantics.MAYBE_BEFORE, Semantics.FOUND]
test_semantics3 = [Semantics.OUT, Semantics.OUT, Semantics.MAYBE_BEFORE, Semantics.MAYBE_BEFORE, Semantics.FOUND_END]
test_semantics4 = [Semantics.OUT, Semantics.OUT, Semantics.MAYBE_BEFORE, Semantics.MAYBE_BEFORE, Semantics.OUT]
test_semantics5 = [Semantics.OUT, Semantics.OUT, Semantics.MAYBE_BEFORE, Semantics.MAYBE_BEFORE, Semantics.FOUND, Semantics.MAYBE_AFTER, Semantics.MAYBE_AFTER, Semantics.IN, Semantics.OUT_RESET, Semantics.OUT ]
test_semantics6 = [Semantics.OUT, Semantics.OUT, Semantics.OUT, Semantics.OUT, Semantics.MAYBE_BEFORE, Semantics.FOUND, Semantics.MAYBE_AFTER, Semantics.OUT_AFTER, Semantics.MAYBE_BEFORE, Semantics.MAYBE_BEFORE, Semantics.FOUND, Semantics.OUT_AFTER, Semantics.MAYBE_BEFORE, Semantics.MAYBE_BEFORE, Semantics.FOUND]

print(find_pattern_occurrences_semantics(test_semantics6))
