from .variable import Variable
class Sound(Variable):
    value = None
    def __init__(self, input):
        self.value = str(input) # TODO: Does that need validation?

    def __str__(self):
        return self.value