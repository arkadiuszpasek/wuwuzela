from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.types.number import Number
from .Element import Element
from .AddComponent import AddComponent


class Equation:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.EquationContext):
        sign = -1 if ctx.MINUS() else 1

        value = AddComponent(variables, ctx.addComponent(0)).value.mult(sign)
        for i, opeator in enumerate(ctx.addOperator()):
            if opeator.MINUS():
                value = value.sub(
                    AddComponent(variables, ctx.addComponent(i + 1)).value
                )
            elif opeator.PLUS():
                value = value.add(
                    AddComponent(variables, ctx.addComponent(i + 1)).value
                )
        self.value = value
