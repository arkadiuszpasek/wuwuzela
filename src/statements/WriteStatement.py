from mingus.midi.midi_file_out import write_NoteContainer
from mingus.midi.midi_file_out import write_Composition
from mingus.midi.midi_file_out import write_Track


from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.statements.CompositionStatement import Composition
from src.types.string import String


class WriteStatement:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.WriteContext):
        comp = Composition(variables, ctx.compositionStatement())

        s = String(ctx.STRING())
        print(s);
        write_Track("example6.mid", comp.nc)
