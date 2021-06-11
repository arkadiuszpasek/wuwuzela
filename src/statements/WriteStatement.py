from mingus.midi.midi_file_out import write_Track

from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.statements.CompositionStatement import Composition
from src.types.string import String
from src.types.tempo import Tempo


def validate_input_file_name(file_name: str):
    splitted = file_name.split('.')
    if len(splitted) != 2 or splitted[1] != 'mid':
        raise RuntimeError('Failed to create file. File name must be specified with mid extension. e.g. "example.mid"')


class WriteStatement:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.WriteContext):
        comp = Composition(variables, ctx.compositionStatement())

        s = String(ctx.STRING())
        s = s.value.replace('"', '')

        try:
            validate_input_file_name(s)
        except RuntimeError as err:
            print(err)
            return
        if ctx.TEMPO():
            tempo = str(ctx.TEMPO())
            number = int(tempo[1:])
            write_Track(s, comp.nc, number)
            return

        write_Track(s, comp.nc)
