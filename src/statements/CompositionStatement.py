from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from mingus.containers import NoteContainer

from src.types.container import Container


class Composition:
    def __init__(self, ctx: Wuwuzela_GrammarParser.CompositionStatementContext):
        self.nc = NoteContainer()

        if ctx.containerStatement():
            print("note container")
            print("container statement")
            container = Container(ctx.containerStatement())

            for i in container.value:
                self.nc.add_note(str(i))

        else:
            print("note variable")
            #NoteContainer(ctx.VARIABLE())
