from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .Comparison import Comparison

class LogicalExpression():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.LogicalExpressionContext):
        value = None
        if ctx.LBRACKET():
            expr = LogicalExpression(variables, ctx.logicalExpression())
            value = expr.value

        elif ctx.trueFalse():
            value = self.handle_trueFalse(ctx.trueFalse())

        elif ctx.comparison():
            comparison = Comparison(variables, ctx.comparison(),
                                    ctx.equation(0) or ctx.element(0), ctx.equation(1) or ctx.element(1))
            value = comparison.value
        elif ctx.NOT():
            expr = LogicalExpression(variables, ctx.logicalExpression(0))
            value = not expr.value
        elif ctx.andOr():
            value = self.handle_andOr(variables, ctx.andOr(), ctx)
        elif ctx.VARIABLE():
            var = variables.get(str(ctx.VARIABLE()))
            value = var.value

        self.value = value

    def handle_trueFalse(self, ctx: Wuwuzela_GrammarParser.TrueFalseContext):
        if ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False

    def handle_andOr(self, variables, ctx: Wuwuzela_GrammarParser.AndOrContext,
                     logical_context: Wuwuzela_GrammarParser.LogicalExpressionContext):
        if ctx.AND():
            expr0 = LogicalExpression(variables, logical_context.logicalExpression(0))
            expr1 = LogicalExpression(variables, logical_context.logicalExpression(1))
            return expr0.value and expr1.value
        elif ctx.OR():
            expr0 = LogicalExpression(variables, logical_context.logicalExpression(0))
            expr1 = LogicalExpression(variables, logical_context.logicalExpression(1))
            return expr0.value or expr1.value

    def __str__(self):
        return str(self.value)
