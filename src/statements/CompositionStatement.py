from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from mingus.containers import NoteContainer

from src.types.container import Container


class Composition:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.CompositionStatementContext):
        self.nc = NoteContainer()

        if ctx.containerStatement():
            container = Container(ctx.containerStatement())

            for i in container.value:
                self.nc.add_note(str(i))

        else:
            container = variables.get(str(ctx.VARIABLE()))

            for i in container.value:
                self.nc.add_note(str(i))
