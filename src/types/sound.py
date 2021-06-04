from .variable import Variable
class Sound(Variable):
    value = None
    def __init__(self, input):
        # if is correct A#Bb etc
        self.value = str(input)

    def __str__(self):
        return self.value