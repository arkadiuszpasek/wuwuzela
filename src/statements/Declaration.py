from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from .VarStatement import VarStatement
from .Statement import Statement

class Declaration():

    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.DeclarationContext):
        if ctx.varStatement():
            VarStatement(variables, ctx.varStatement())
        elif ctx.statement():
            Statement(variables, ctx.statement())