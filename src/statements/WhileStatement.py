from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.expressions.LogicalExpression import LogicalExpression


class WhileStatement():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.WhileLoopContext):
        from .Declaration import Declaration
        logical_expr = ctx.logicalExpression()

        while LogicalExpression(variables, logical_expr).value:
            for i, declaration in enumerate(ctx.declaration()):
                print("iterator: ", i)
                print("declaration: ", declaration)
                Declaration(self.variables, declaration)