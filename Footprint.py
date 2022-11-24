from cmath import inf
from Enums.Aggregators import Aggregators
from Enums.Semantics import Semantics
from FootprintElem import FootprintElem


def footprint(semantics):
    p = [[0]] * len(semantics)
    C = 0

    i = 0
    while i < len(semantics):
        match semantics[i]:
            case Semantics.OUT | Semantics.OUT_RESET | Semantics.OUT_AFTER:
                p[i] = FootprintElem(0)
            case Semantics.MAYBE_BEFORE | Semantics.MAYBE_AFTER:
                p[i] = FootprintElem("p[" + (i+1).__str__() + "]")
            case Semantics.FOUND | Semantics.FOUND_END:
                p[i] = FootprintElem(C+1)
                C += 1
            case Semantics.IN:
                p[i] = FootprintElem(C)
        i += 1

    i = len(semantics)-1
    while i >= 0:
        p[i].update_elem(p)
        i -= 1

    return p

"""def guard(semantics,feature,aggregator,pattern):
    f = []
    ct = []
    at = []
    r = 0
    c = 0

    i = 0
    while i < len(semantics):
        match semantics[i]:
            case Semantics.OUT | Semantics.OUT_RESET:
                f[i] = 0
                ct[i+1] = ct[i]
                at[i+1] = at[i]
            case Semantics.OUT_AFTER:
                if comparator_g(aggregator, c, r):
                    f[i] = 0
                    at[i] = 0
                    at[i+1] = ct[i]
                if c == r :
                    f[i] = 0
                    at[i+1] = ct[i]
                    at[i+1] = at[i]
                if comparator_g(aggregator, r, c):
                    f[i] = 0
                    ct[i] = 0
                    at[i+1] = at[i]
            case Semantics.MAYBE_BEFORE:
                f[i] = 0
                ct[i+1] = ct[i]
                at[i+1] = at[i]
            case Semantics.MAYBE_AFTER:
                f[i] = 0
                ct[i+1] = ct[i]
                at[i+1] = at[i]
            case Semantics.FOUND:
                ct[i] = 0
                ct[i+1] = f[i]
                at[i+1] = at[i]
            case Semantics.IN:
                f[i] = 0
                ct[i+1] = ct[i]
                at[i+1] = at[i]
            case Semantics.FOUND_END:
                print(semantics[i])


def comparator_g(aggregator, val1, val2):
    if aggregator == Aggregators.MAX:
        return val1 > val2
    elif aggregator == Aggregators.MIN:
        return val1 < val2"""
