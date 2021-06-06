from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .PrintStatement import PrintStatement
from .IfStatement import IfStatement
from .WriteStatement import WriteStatement


class Statement():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.StatementContext):
        if ctx.printStatement():
            PrintStatement(variables, ctx.printStatement())
        elif ctx.ifStatement():
            IfStatement(variables, ctx.ifStatement())
        elif ctx.write():
            WriteStatement(ctx.write())
        # TODO: finish the rest of statements