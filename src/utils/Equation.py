from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .VariableTracker import VariableTracker
from src.types.number import Number

class Equation():
    def __init__(self, variables: VariableTracker, ctx: Wuwuzela_GrammarParser.EquationContext):
        left: Wuwuzela_GrammarParser.ElementContext = ctx.element(0)
        right: Wuwuzela_GrammarParser.ElementContext = ctx.element(1)
        maybe_left_number = Number(left.NUMBER()) if left.NUMBER() else None
        maybe_left_variable = left.VARIABLE()
        maybe_right_number = Number(right.NUMBER()) if right.NUMBER() else None
        maybe_right_variable = right.VARIABLE()
        if maybe_left_variable:
            maybe_left_number = variables.get(str(maybe_left_variable))
        if maybe_right_variable:
            maybe_right_number = variables.get(str(maybe_right_variable))

        print(f'{maybe_left_number}, {maybe_right_number}')
        if maybe_left_number == None or type(maybe_left_number) != Number \
            or maybe_right_number == None or type(maybe_right_number) != Number:
            raise ValueError(f'Incorrect values in equation {ctx.getText()}. Left {maybe_left_number},\
                right {maybe_right_number}')

        self.value = equate(maybe_left_number, maybe_right_number, ctx.mathOperation())

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
