from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser


class BracketEquation:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.BracketEquationContext):
        from .Equation import Equation

        self.value = Equation(variables, ctx.equation()).value
