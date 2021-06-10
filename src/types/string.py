class String():
    def __init__(self, input):
        self.value = str(input)
        print(type(self.value))

    def __str__(self):
        return self.value