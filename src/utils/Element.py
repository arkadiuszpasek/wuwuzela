from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.types.number import Number

class Element():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.ElementContext):
        value = Number(ctx.NUMBER()) if ctx.NUMBER() else None
        maybe_variable = ctx.VARIABLE()
        if maybe_variable:
            value = variables.get(str(maybe_variable))

        self.value = value
