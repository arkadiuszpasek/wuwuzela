from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from mingus.containers import NoteContainer
from mingus.containers import Composition as Composition_Mingus
from mingus.containers import Bar, Track

from src.types.container import Container

NOTE_DURATION = 16


class Composition:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.CompositionStatementContext):
        self.nc = Track()

        if ctx.containerStatement():
            container = Container(ctx.containerStatement())
            for item in container.value:
                self.nc.add_notes(str(item), NOTE_DURATION)

        else:
            container = variables.get(str(ctx.VARIABLE()))
            for item in container.value:
                self.nc.add_notes(str(item), NOTE_DURATION)
