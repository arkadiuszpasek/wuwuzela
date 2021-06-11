from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.expressions.LogicalExpression import LogicalExpression


class IfStatement:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.IfStatementContext):
        global i
        from .Declaration import Declaration

        logical_expr = ctx.logicalExpression()

        if LogicalExpression(variables, logical_expr).value:
            for declaration in ctx.declaration():
                Declaration(variables, declaration)

            if ctx.RBRACE():
                return
