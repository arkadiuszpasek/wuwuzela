from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .Comparison import Comparison

class LogicalExpression():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.LogicalExpressionContext):
        if ctx.trueFalse():
            self.handle_trueFalse(ctx.trueFalse())
        elif ctx.comparison():
            comparison = Comparison(variables, ctx.comparison(),
                ctx.equation(0) or ctx.element(0), ctx.equation(1) or ctx.element(1))
            self.value = comparison.value



    def handle_trueFalse(self, ctx: Wuwuzela_GrammarParser.TrueFalseContext):
        if ctx.TRUE():
            self.value = True
        elif ctx.FALSE():
            self.value = False

    def __str__(self):
        return str(self.value)
