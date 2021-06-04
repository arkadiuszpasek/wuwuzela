from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .Comparison import Comparison

class LogicalExpression():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.LogicalExpressionContext):
        value = None
        if ctx.trueFalse():
            value = self.handle_trueFalse(ctx.trueFalse())
        elif ctx.comparison():
            comparison = Comparison(variables, ctx.comparison(),
                ctx.equation(0) or ctx.element(0), ctx.equation(1) or ctx.element(1))
            value = comparison.value
        elif ctx.NOT():
            expr = LogicalExpression(variables, ctx.logicalExpression(0))
            value = not expr.value
            
        # TODO: brackets, AND OR
        self.value = value


    def handle_trueFalse(self, ctx: Wuwuzela_GrammarParser.TrueFalseContext):
        if ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False

    def __str__(self):
        return str(self.value)
