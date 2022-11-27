"""from Enums.Semantics import Semantics
from GuardValue import Pointer


def footprint(semantics):
    p = [[0]] * len(semantics)
    C = 0

    i = 0
    while i < len(semantics):
        match semantics[i]:
            case Semantics.OUT | Semantics.OUT_RESET | Semantics.OUT_AFTER:
                p[i] = Pointer(0)
            case Semantics.MAYBE_BEFORE | Semantics.MAYBE_AFTER:
                p[i] = Pointer("p[" + (i+1).__str__() + "]")
            case Semantics.FOUND | Semantics.FOUND_END:
                p[i] = Pointer(C+1)
                C += 1
            case Semantics.IN:
                p[i] = Pointer(C)
        i += 1

    i = len(semantics)-1
    while i >= 0:
        p[i].update(p)
        i -= 1

    return p"""