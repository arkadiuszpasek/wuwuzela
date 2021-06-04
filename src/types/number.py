
class Number():
    value = None
    def __init__(self, input):
        self.value = float(str(input))

    def __str__(self):
        return str(self.value)