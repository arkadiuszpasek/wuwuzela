from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from mingus.containers import NoteContainer
from mingus.containers import Composition as Composition_Mingus
from mingus.containers import Bar

from src.types.container import Container


class Composition:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.CompositionStatementContext):
        # self.nc = NoteContainer()
        # self.nc = Composition_Mingus()
        self.nc = Bar()


        if ctx.containerStatement():
            container = Container(ctx.containerStatement())

            for i in container.value:

                self.nc.add_note(str(i))

        else:
            container = variables.get(str(ctx.VARIABLE()))

            for i in container.value:
                # i_converted = str(i) + '-4'
                # print(i_converted)
                self.nc.place_notes(str(i),16)
