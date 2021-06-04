from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.types.sound import Sound
from src.types.number import Number
from src.types.container import Container
from .LogicalExpression import LogicalExpression

class VariableTracker():
    values = {}
    def get(self, name):
        return self.values[name]

    def new(self, name, ctx: Wuwuzela_GrammarParser.VarStatementContentContext):
        self.values[name] = self.ctxToValue(ctx)
    
    def update(self, name, value):
        if name in self:
            self[name] = value
        # else:
            # exit with error undefined reference? but that's probably not possible to get from parser

    def ctxToValue(self, ctx: Wuwuzela_GrammarParser.VarStatementContentContext):
        maybe_number = ctx.NUMBER()
        if maybe_number:
            return Number(maybe_number)
        
        maybe_sound = ctx.SOUND()
        if maybe_sound:
            return Sound(maybe_sound)

        maybe_variable = ctx.VARIABLE()
        if maybe_variable and maybe_variable in self.values:
            return self.values[maybe_variable]

        maybe_container = ctx.containerStatement()
        if maybe_container:
            return Container(maybe_container)
        
        maybe_logical_expr = ctx.logicalExpression()
        if maybe_logical_expr:
            return LogicalExpression(self, maybe_logical_expr)

        raise TypeError(f'Cannot assign to variable: {ctx.getText()}')
    
    