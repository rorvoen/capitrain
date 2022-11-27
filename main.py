from math import inf

from GeneratedFunctions import pos_max_max_peak
from Testing import testing
from TimeSeriesParser import *
from GenerateFunctions import *
from Enums.Semantics import Semantics


"""test_sequence = [4, 4, 2, 2, 3, 5, 5, 6, 3, 1, 1, 2, 2, 2, 2, 2, 2, 1]
print(test_sequence)

test_signature = time_series_to_signature_parser(test_sequence)
print(test_signature)

test_semantics = signature_to_semantic(test_signature, Patterns.PEAK)
print(test_semantics)

test_result = pos_max_max_peak(test_sequence)
print(test_result)"""


#generate_functions()
testing()

#write_guard_lines(Semantics.FOUND_END, "1", "max", "max", 3)


# TODO : Update testing
# TODO : Ecrire la doc
# TODO : Ne pas générer les méthodes en trop
