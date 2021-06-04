
class Variable():
    value = None

    def __init__(self):
        pass

    def add(self, value):
        raise TypeError(f'Addition not possible on this type of variable {type(self)}')
    def sub(self, value):
        raise TypeError(f'Subtraction not possible on this type of variable {type(self)}')
        pass
    def mult(self, value):
        raise TypeError(f'Multiplication not possible on this type of variable {type(self)}')
        pass
    def div(self, value):
        raise TypeError(f'Division not possible on this type of variable {type(self)}')
        pass