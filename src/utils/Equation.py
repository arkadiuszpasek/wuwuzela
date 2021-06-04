from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.types.Number import Number
from .Element import Element

class Equation():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.EquationContext):
        left = Element(variables, ctx.element(0))
        right = Element(variables, ctx.element(1))

        isLeftIncorrect = left.value == None or type(left.value) != Number
        isRightIncorrect = right.value == None or type(right.value) != Number
        if isLeftIncorrect and isRightIncorrect:
            raise ValueError(
                f'Incorrect values in equation {ctx.getText()}. Left {left.value},right {right.value}'
            )

        self.value = equate(left.value, right.value, ctx.mathOperation())

def equate(left: Number, right: Number, ctx: Wuwuzela_GrammarParser.MathOperationContext):
    if ctx.PLUS():
        return left.add(right)
    if ctx.MINUS():
        return left.sub(right) # TODO: This doesn't work, but that's a problem with a grammar probably
    if ctx.MULTIPLY():
        return left.mult(right)
    if ctx.DIVIDE():
        return left.div(right)
