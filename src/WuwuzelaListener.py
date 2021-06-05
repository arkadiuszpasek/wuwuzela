from antlr4 import *

from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from grammar.Wuwuzela_GrammarListener import Wuwuzela_GrammarListener
from .utils.VariableTracker import VariableTracker
from src.expressions.Equation import Equation
from .statements.PrintStatement import PrintStatement
from .statements.Declaration import Declaration


class WuwuzelaListener(Wuwuzela_GrammarListener):
    variables = VariableTracker()

    def enterMusicProgram(self, ctx: Wuwuzela_GrammarParser.MusicProgramContext):
        for declaration in ctx.declaration():
            Declaration(self.variables, declaration)
