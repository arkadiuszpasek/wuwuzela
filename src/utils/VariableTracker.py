from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.types.sound import Sound
from src.types.number import Number
from src.types.container import Container
from .LogicalExpression import LogicalExpression

class VariableTracker():
    values = {}
    def get(self, name):
        if not name in self.values:
            raise ValueError(f'Value {name} does not exist')
        return self.values[name]

    def new(self, name, ctx: Wuwuzela_GrammarParser.VarStatementContentContext):
        self.values[name] = self.ctxToValue(ctx)
    
    # TODO: do we event allow variable reassignment?
    def update(self, name, value):
        if name in self:
            self[name] = value

    def ctxToValue(self, ctx: Wuwuzela_GrammarParser.VarStatementContentContext):
        if ctx.NUMBER():
            return Number(ctx.NUMBER())
        
        if ctx.SOUND():
            return Sound(ctx.SOUND())

        if ctx.VARIABLE() and ctx.VARIABLE() in self.values:
            return self.values[ctx.VARIABLE()]

        if ctx.containerStatement():
            return Container(ctx.containerStatement())
        
        if ctx.logicalExpression():
            return LogicalExpression(self, ctx.logicalExpression())

        raise TypeError(f'Cannot assign to variable: {ctx.getText()}')
    
    