from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.types.number import Number
from .Element import Element
from .MulFactor import MulFactor


class AddComponent:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.AddComponentContext):
        value = MulFactor(variables, ctx.mulFactor(0)).value

        for i, operator in enumerate(ctx.mulOperator()):
            if operator.MULTIPLY():
                value = value.mult(MulFactor(variables, ctx.mulFactor(i + 1)).value)
            elif operator.DIVIDE():
                value = value.div(MulFactor(variables, ctx.mulFactor(i + 1)).value)
        self.value = value
