from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .VariableTracker import VariableTracker
from src.types.number import Number
from .Element import Element

class Equation():
    def __init__(self, variables: VariableTracker, ctx: Wuwuzela_GrammarParser.EquationContext):
        left = Element(variables, ctx.element(0))
        right = Element(variables, ctx.element(1))
        if left.value == None or type(left.value) != Number \
            or right.value == None or type(right.value) != Number:
            raise ValueError(f'Incorrect values in equation {ctx.getText()}. Left {left.value},\
                right {right.value}')

        self.value = equate(left.value, right.value, ctx.mathOperation())

def equate(left: Number, right: Number, ctx: Wuwuzela_GrammarParser.MathOperationContext):
    if ctx.PLUS():
        return left.add(right)
    if ctx.MINUS():
        print('miNUS')
        return left.sub(right)
    if ctx.MULTIPLY():
        return left.mult(right)
    if ctx.DIVIDE():
        return left.div(right)
