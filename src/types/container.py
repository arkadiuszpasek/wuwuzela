from .Variable import Variable
from .Sound import Sound
from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser

class Container(Variable):
    def __init__(self, ctx: Wuwuzela_GrammarParser.ContainerStatementContext):
        content: Wuwuzela_GrammarParser.ContainerContentContext = ctx.containerContent()

        values = []
        for s in content.SOUND():
            values.append(Sound(s))

        self.value = values

    def __str__(self):
        return '[' + ', '.join(list(map(lambda x: str(x), self.value))) + ']'