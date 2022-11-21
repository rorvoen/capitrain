from enum import Enum


class Semantics(Enum):
    FOUND = "found"
    FOUND_END = "found_e"
    MAYBE_BEFORE = "maybe_b"
    OUT_RESET = "out_r"
    IN = "in"
    MAYBE_AFTER = "maybe_a"
    OUT_AFTER = "out_a"
    OUT = "out"

    def __str__(self):
        return self.name
