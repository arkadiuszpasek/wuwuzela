from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser

class LogicalExpression():
    def __init__(self, variable, ctx: Wuwuzela_GrammarParser.LogicalExpressionContext):
        maybe_trueFalse: Wuwuzela_GrammarParser.TrueFalseContext = ctx.trueFalse()
        if maybe_trueFalse:
            self.handle_trueFalse(maybe_trueFalse)



    def handle_trueFalse(self, ctx: Wuwuzela_GrammarParser.TrueFalseContext):
        if ctx.TRUE():
            self.value = True
        elif ctx.FALSE():
            self.value = False

    def __str__(self):
        return str(self.value)
