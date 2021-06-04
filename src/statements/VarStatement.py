from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser

class VarStatement():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.VarStatementContext):
        variables.new(str(ctx.VARIABLE()), ctx.varStatementContent())
