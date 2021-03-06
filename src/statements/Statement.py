from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .AddSoundToContainerStatement import AddSoundToContainerStatement
from .PrintStatement import PrintStatement
from .IfStatement import IfStatement
from .WhileStatement import WhileStatement
from .WriteStatement import WriteStatement
from .TransposeStatement import TransposeStatement


class Statement():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.StatementContext):
        if ctx.printStatement():
            PrintStatement(variables, ctx.printStatement())
        elif ctx.ifStatement():
            IfStatement(variables, ctx.ifStatement())
        elif ctx.whileLoop():
            WhileStatement(variables, ctx.whileLoop())
        elif ctx.write():
            WriteStatement(variables, ctx.write())
        elif ctx.transposeStatement():
            TransposeStatement(variables, ctx.transposeStatement())
        elif ctx.addSoundToContainerStatement():
            AddSoundToContainerStatement(variables, ctx.addSoundToContainerStatement())
        # TODO: finish the rest of statements