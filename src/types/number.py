from .Variable import Variable

class Number(Variable):
    value = None
    def __init__(self, input):
        self.value = float(str(input))

    def __str__(self):
        return str(self.value)

    def add(self, value):
        if (type(value) == Number):
            return self.value + value.value
        raise TypeError(f'Value of type ${type(value)} cannot be used in number.add')

    def sub(self, value):

        print('subbi')
        if (type(value) == Number):
            return self.value - value.value
        raise TypeError(f'Value of type ${type(value)} cannot be used in number.sub')

    def mult(self, value):
        if (type(value) == Number):
            return self.value * value.value
        raise TypeError(f'Value of type ${type(value)} cannot be used in number.mult')

    def div(self, value):
        if (type(value) == Number):
            return self.value / value.value
        raise TypeError(f'Value of type ${type(value)} cannot be used in number.div')