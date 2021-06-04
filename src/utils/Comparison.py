from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .Element import Element
from .Equation import Equation
from src.types.Number import Number

class Comparison():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.ComparisonContext, left, right):
        if type(left) == Wuwuzela_GrammarParser.ElementContext and type(right) == Wuwuzela_GrammarParser.ElementContext:
            self.handle_element_comparison(variables, ctx, left, right)

        if type(left) == Wuwuzela_GrammarParser.EquationContext and type(right) == Wuwuzela_GrammarParser.EquationContext:
            self.handle_equation_comparison(variables, ctx, left, right)
        

    def handle_equation_comparison(self, variables, ctx: Wuwuzela_GrammarParser.ComparisonContext,
        left_ctx: Wuwuzela_GrammarParser.EquationContext, right_ctx: Wuwuzela_GrammarParser.EquationContext):
            left = Equation(variables, left_ctx).value
            right = Equation(variables, right_ctx).value

            if ctx.EQUAL():
                self.value = left.value == right.value
            elif ctx.GREATER():
                self.value = left.value > right.value
            elif ctx.GREATER_EQUAL():
                self.value = left.value >= right.value
            elif ctx.LESS():
                self.value = left.value < right.value
            elif ctx.LESS_EQUAL():
                self.value = left.value <= right.value

    def handle_element_comparison(self, variables, ctx: Wuwuzela_GrammarParser.ComparisonContext,
        left_ctx: Wuwuzela_GrammarParser.ElementContext, right_ctx: Wuwuzela_GrammarParser.ElementContext):
            left: Number = Element(variables, left_ctx).value
            right: Number = Element(variables, right_ctx).value

            if ctx.EQUAL():
                self.value = left.value == right.value
            elif ctx.GREATER():
                self.value = left.value > right.value
            elif ctx.GREATER_EQUAL():
                self.value = left.value >= right.value
            elif ctx.LESS():
                self.value = left.value < right.value
            elif ctx.LESS_EQUAL():
                self.value = left.value <= right.value


