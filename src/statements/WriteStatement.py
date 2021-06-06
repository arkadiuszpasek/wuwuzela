from mingus.containers import NoteContainer
from mingus.midi.midi_file_out import write_NoteContainer

from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.statements.CompositionStatement import Composition


class WriteStatement:
    def __init__(self, ctx: Wuwuzela_GrammarParser.WriteContext):
        # print("Write as midi")
        # print("string: ")
        # print(ctx.STRING())
        # print("composition: ")
        # print(str(ctx.compositionStatement()))
        # nc = NoteContainer(["A", "C", "E"])
        #print(NoteContainer(["A", "C", "E"]))
        comp = Composition(ctx.compositionStatement())
        write_NoteContainer("example1.mid", comp.nc)