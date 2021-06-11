from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.types.container import Container
from mingus.containers import Note
import mingus.core.notes as notes

TRANSPOSITION_COUNT = "2"


class TransposeStatement:
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.TransposeStatementContext):
        if ctx.VARIABLE():
            var = variables.get(str(ctx.VARIABLE()))
            for idx, note in enumerate(var.value):
                temp = Note(note)
                if temp.octave < 0 or temp.octave + int(TRANSPOSITION_COUNT) > 7:
                    # if octave is out of range or transposing note TRANSPOSITION_COUNT times goes out of range
                    pass
                else:
                    temp.transpose(TRANSPOSITION_COUNT)
                var.value[idx] = str(temp).replace("'", "")
        elif ctx.containerStatement():
            container = Container(ctx.containerStatement())
            for idx, note in enumerate(container.value):
                temp = Note(note)
                if temp.octave < 0 or temp.octave + int(TRANSPOSITION_COUNT) > 7:
                    # if octave is out of range or transposing note TRANSPOSITION_COUNT times goes out of range
                    pass
                else:
                    temp.transpose(TRANSPOSITION_COUNT)
                container.value[idx] = str(temp).replace("'", "")
