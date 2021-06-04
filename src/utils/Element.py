from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.types.Number import Number

class Element():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.ElementContext):
        value = Number(ctx.NUMBER()) if ctx.NUMBER() else None

        if ctx.VARIABLE():
            value = variables.get(str(ctx.VARIABLE()))

        self.value = value
