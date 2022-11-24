import re


class FootprintElem:
    def __init__(self, value):
        self.value = value

    def update_elem(self, p_array):
        if (not isinstance(self.value, int)) & (not isinstance(self.value, float)):
            match = re.search(r"p\[([0-9]+)\]", self.value)
            if not (match is None):
                value_index = int(match.group(1))
                self.value = p_array[value_index].value

    def __str__(self):
        return self.value.__str__()

    def __repr__(self):
        return self.__str__()
