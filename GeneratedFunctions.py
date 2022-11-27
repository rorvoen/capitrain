from math import inf
from Enums.Patterns import Patterns
from GuardValue import GuardValue
from TimeSeriesParser import *


def pos_max_max_bump_on_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.BUMP_ON_DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_decreasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_decreasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_TERRACE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_dip_on_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DIP_ON_INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_gorge(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.GORGE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_increasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_increasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_TERRACE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_inflexion(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INFLEXION)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_peak(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PEAK)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLAIN)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLATEAU)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_proper_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLAIN)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_proper_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLATEAU)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_steady(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_steady_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_strictly_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_strictly_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_summit(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.SUMMIT)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_valley(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.VALLEY)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_max_zigzag(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.ZIGZAG)
    default_g_f = -inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_bump_on_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.BUMP_ON_DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_decreasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_decreasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_TERRACE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_dip_on_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DIP_ON_INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_gorge(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.GORGE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_increasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_increasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_TERRACE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_inflexion(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INFLEXION)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_peak(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PEAK)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLAIN)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLATEAU)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_proper_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLAIN)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_proper_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLATEAU)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_steady(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_steady_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_strictly_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_DECREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_strictly_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_INCREASING_SEQUENCE)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_summit(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.SUMMIT)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_valley(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.VALLEY)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_max_min_zigzag(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.ZIGZAG)
    default_g_f = -inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) > R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C > R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R > C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = max(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C > R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R > C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return max(R,C), time_series, f


def pos_min_max_bump_on_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.BUMP_ON_DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_decreasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_decreasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_TERRACE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_dip_on_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DIP_ON_INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_gorge(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.GORGE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_increasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_increasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_TERRACE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_inflexion(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INFLEXION)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_peak(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PEAK)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLAIN)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLATEAU)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_proper_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLAIN)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_proper_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLATEAU)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_steady(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_steady_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_strictly_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_strictly_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(delta_f_1, (max(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if max(max(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(max(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(max(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(delta_f_1, (max(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_summit(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.SUMMIT)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_valley(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.VALLEY)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_max_zigzag(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.ZIGZAG)
    default_g_f = inf
    neutral_f = -inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if max(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if max(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < max(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = max(C, (max(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = max(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_bump_on_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.BUMP_ON_DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_decreasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_decreasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DECREASING_TERRACE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_dip_on_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.DIP_ON_INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_gorge(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.GORGE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_increasing(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_increasing_terrace(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INCREASING_TERRACE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_inflexion(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.INFLEXION)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_peak(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PEAK)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLAIN)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PLATEAU)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_proper_plain(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLAIN)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_proper_plateau(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.PROPER_PLATEAU)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_steady(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_steady_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STEADY_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_strictly_decreasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_DECREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_strictly_increasing_sequence(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.STRICTLY_INCREASING_SEQUENCE)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(delta_f_1, (min(D, delta_f)))

                D = neutral_f

            case Semantics.FOUND_END:
                if min(min(D,delta_f),delta_f_1) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(min(D,delta_f),delta_f_1) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(min(D,delta_f),delta_f_1):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(delta_f_1, (min(D, delta_f)))))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f_1)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f_1)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_summit(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.SUMMIT)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_valley(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.VALLEY)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


def pos_min_min_zigzag(time_series):
    signature = time_series_to_signature_parser(time_series)
    semantics = signature_to_semantic(signature, Patterns.ZIGZAG)
    default_g_f = inf
    neutral_f = inf

    R = default_g_f
    C = default_g_f
    D = neutral_f

    at = [GuardValue(0)]*len(time_series)
    ct = [GuardValue(0)]*len(time_series)
    f = [GuardValue(0)]*len(time_series)

    i = 0

    for word in semantics:
        delta_f = time_series[i]
        delta_f_1 = time_series[i+1]
        match word:
            case Semantics.FOUND:
                ct[i] = GuardValue(0)
                f[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(D, delta_f)

                D = neutral_f

            case Semantics.FOUND_END:
                if min(D,delta_f) < R:
                    f[i] = GuardValue(float(inf), ct, i, "ct")
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if min(D,delta_f) == R:
                    f[i] = GuardValue(float(inf), at, i+1, "at")
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < min(D,delta_f):
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_BEFORE:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_RESET:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = neutral_f

            case Semantics.IN:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                C = min(C, (min(D, delta_f)))

                D = neutral_f

            case Semantics.MAYBE_AFTER:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

                D = min(D, delta_f)

            case Semantics.OUT_AFTER:
                if C < R:
                    f[i] = GuardValue(0)
                    at[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                if C == R:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(float(inf), at, i+1, "at")
                    at[i] = GuardValue(float(inf), at, i+1, "at")
                if R < C:
                    f[i] = GuardValue(0)
                    ct[i] = GuardValue(0)
                    at[i] = GuardValue(float(inf), at, i+1, "at")

                R = min(R, C)

                C = default_g_f

                D = neutral_f

            case Semantics.OUT:
                f[i] = GuardValue(0)
                ct[i] = GuardValue(float(inf), ct, i+1, "ct")
                at[i] = GuardValue(float(inf), at, i+1, "at")

        i += 1 

    f[len(time_series) - 1] = GuardValue(0)
    if C < R:
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R == default_g_f):
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(0)
    elif (C == R) & (R != default_g_f):
        ct[len(time_series) - 1] = GuardValue(1)
        at[len(time_series) - 1] = GuardValue(1)
    elif R < C:
        ct[len(time_series) - 1] = GuardValue(0)
        at[len(time_series) - 1] = GuardValue(1)


    return min(R,C), time_series, f


