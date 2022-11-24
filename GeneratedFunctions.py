from math import inf
from Enums.Patterns import Patterns
from TimeSeriesParser import *


def pos_max_max_bump_on_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.BUMP_ON_DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_decreasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_decreasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_TERRACE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_dip_on_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DIP_ON_INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_gorge(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.GORGE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_increasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_increasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_TERRACE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_inflexion(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INFLEXION)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_peak(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PEAK)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLAIN)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLATEAU)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_proper_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLAIN)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_proper_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLATEAU)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_steady(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_steady_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_strictly_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_strictly_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_summit(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.SUMMIT)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_valley(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.VALLEY)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_max_zigzag(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.ZIGZAG)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_bump_on_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.BUMP_ON_DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_decreasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_decreasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_TERRACE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_dip_on_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DIP_ON_INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_gorge(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.GORGE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_increasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_increasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_TERRACE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_inflexion(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INFLEXION)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_peak(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PEAK)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLAIN)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLATEAU)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_proper_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLAIN)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_proper_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLATEAU)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_steady(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_steady_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_strictly_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_strictly_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_summit(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.SUMMIT)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_valley(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.VALLEY)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_max_min_zigzag(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.ZIGZAG)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = max(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) > R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = max(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C > R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R > C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return max(R, C)


def pos_min_max_bump_on_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.BUMP_ON_DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_decreasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_decreasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_TERRACE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_dip_on_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DIP_ON_INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_gorge(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.GORGE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_increasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_increasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_TERRACE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_inflexion(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INFLEXION)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_peak(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PEAK)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLAIN)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLATEAU)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_proper_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLAIN)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_proper_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLATEAU)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_steady(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_steady_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_strictly_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_strictly_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(delta_f_1), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(delta_f_1), (max(float(D), float(delta_f))))))

                D = float(neutral_f)

                if max(max(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(max(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_summit(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.SUMMIT)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_valley(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.VALLEY)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_max_zigzag(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.ZIGZAG)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = max(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                if max(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if max(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < max(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = max(float(C), (max(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = max(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_bump_on_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.BUMP_ON_DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_decreasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_decreasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_TERRACE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_dip_on_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DIP_ON_INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_gorge(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.GORGE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_increasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_increasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_TERRACE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_inflexion(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INFLEXION)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_peak(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PEAK)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLAIN)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLATEAU)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_proper_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLAIN)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_proper_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLATEAU)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_steady(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_steady_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_strictly_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_strictly_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(delta_f_1), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(delta_f_1), (min(float(D), float(delta_f))))))

                D = float(neutral_f)

                if min(min(D,delta_f),delta_f_1) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(min(D,delta_f),delta_f_1) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f_1))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f_1))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_summit(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.SUMMIT)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_valley(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.VALLEY)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


def pos_min_min_zigzag(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.ZIGZAG)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [0]*len(time_series)
    ct = [0]*len(time_series)
    f = [0]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                C = min(float(D), float(delta_f))

                D = float(neutral_f)

                ct[i] = float(0)
                ct[i+1] = float(f[i])
                at[i+1] = float(at[i])

            case Semantics.FOUND_END:
                R = min(float(R), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                if min(D,delta_f) < R:
                    ct[i] = float(f[i])
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if min(D,delta_f) == R:
                    at[i+1] = float(f[i])
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < min(D,delta_f):
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

            case Semantics.MAYBE_BEFORE:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_RESET:
                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.IN:
                C = min(float(C), (min(float(D), float(delta_f))))

                D = float(neutral_f)

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.MAYBE_AFTER:
                D = min(float(D), float(delta_f))

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

            case Semantics.OUT_AFTER:
                R = min(float(R), float(C))

                C = float(default_g_f)

                D = float(neutral_f)

                if C < R:
                    f[i] = float(0)
                    at[i] = float(0)
                    at[i+1] = float(ct[i])
                if C == R:
                    f[i] = float(0)
                    at[i+1] = float(ct[i])
                    at[i+1] = float(at[i])
                if R < C:
                    f[i] = float(0)
                    ct[i] = float(0)
                    at[i+1] = float(at[i])

                f[i] = float(0)
                ct[i+1] = float(ct[i])
                at[i+1] = float(at[i])

        i += 1 

    return min(R, C)


