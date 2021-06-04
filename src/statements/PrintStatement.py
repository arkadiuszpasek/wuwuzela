from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.expressions.Equation import Equation

class PrintStatement():
    def __init__(self, variables, ctx: Wuwuzela_GrammarParser.PrintStatementContext):
        value: Wuwuzela_GrammarParser.ValueContext = ctx.value()
        
        if value.STRING():
            print(str(value.STRING()))
            return

        if value.VARIABLE():
            print(str(variables.get(str(value.VARIABLE()))))
            return
        
        if value.equation():
            print(Equation(variables, value.equation()).value)
            return

        raise TypeError(f'Cannot print {ctx.getText()}')