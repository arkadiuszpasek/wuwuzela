from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .Element import Element
from .BracketEquation import BracketEquation


class MulFactor:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.MulFactorContext):
        if ctx.element():
            self.value = Element(variables, ctx.element()).value
        elif ctx.bracketEquation():
            self.value = BracketEquation(variables, ctx.bracketEquation()).value
