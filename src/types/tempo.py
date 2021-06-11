from .variable import Variable


class Tempo():
    value = None

    def __init__(self, input):
        self.value = input

    def __str__(self):
        return f"Tempo({self.value})"
