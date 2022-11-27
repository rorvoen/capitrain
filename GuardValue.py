import re
from math import inf


class GuardValue:

    def __init__(self, value, *args):
        self.value = value
        if len(args) > 0:
            self.connected_table = args[0]
            self.index = args[1]

    def get(self):
        if not (self.value == float(inf)):
            return self.value
        else:
            return self.connected_table[self.index].get()

    def __str__(self):
        return self.get().__str__()

    def __repr__(self):
        return self.__str__()
