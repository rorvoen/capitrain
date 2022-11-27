from enum import Enum

# This enumeration represent the different available patterns


class Patterns(Enum):
    BUMP_ON_DECREASING_SEQUENCE = "bump_on_decreasing_sequence"
    DECREASING = "decreasing"
    DECREASING_SEQUENCE = "decreasing_sequence"
    DECREASING_TERRACE = "decreasing_terrace"
    DIP_ON_INCREASING_SEQUENCE = "dip_on_increasing_sequence"
    GORGE = "gorge"
    INCREASING = "increasing"
    INCREASING_SEQUENCE = "increasing_sequence"
    INCREASING_TERRACE = "increasing_terrace"
    INFLEXION = "inflexion"
    PEAK = "peak"
    PLAIN = "plain"
    PLATEAU = "plateau"
    PROPER_PLAIN = "proper_plain"
    PROPER_PLATEAU = "proper_plateau"
    STEADY = "steady"
    STEADY_SEQUENCE = "steady_sequence"
    STRICTLY_DECREASING_SEQUENCE = "strictly_decreasing_sequence"
    STRICTLY_INCREASING_SEQUENCE = "strictly_increasing_sequence"
    SUMMIT = "summit"
    VALLEY = "valley"
    ZIGZAG = "zigzag"



