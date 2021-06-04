from antlr4 import *

from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from grammar.Wuwuzela_GrammarListener import Wuwuzela_GrammarListener
from .utils.VariableTracker import VariableTracker
from .utils.Equation import Equation
class WuwuzelaListener(Wuwuzela_GrammarListener):
    variables = VariableTracker()
    def enterMusicProgram(self, ctx:Wuwuzela_GrammarParser.MusicProgramContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#musicProgram.
    def exitMusicProgram(self, ctx:Wuwuzela_GrammarParser.MusicProgramContext):
        for k in self.variables.values:
            print(f'{k} - - {self.variables.values[k]}')


    # Enter a parse tree produced by Wuwuzela_GrammarParser#declaration.
    def enterDeclaration(self, ctx:Wuwuzela_GrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#declaration.
    def exitDeclaration(self, ctx:Wuwuzela_GrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#statement.
    def enterStatement(self, ctx:Wuwuzela_GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#statement.
    def exitStatement(self, ctx:Wuwuzela_GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#whileLoop.
    def enterWhileLoop(self, ctx:Wuwuzela_GrammarParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#whileLoop.
    def exitWhileLoop(self, ctx:Wuwuzela_GrammarParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#printStatement.
    def enterPrintStatement(self, ctx:Wuwuzela_GrammarParser.PrintStatementContext):
        value: Wuwuzela_GrammarParser.ValueContext = ctx.value()
        
        maybe_str = value.STRING()
        if maybe_str:
            print(str(maybe_str))
            return

        maybe_variable = value.VARIABLE()
        if maybe_variable:
            print(str(self.variables.get(str(maybe_variable))))
            return
        
        maybe_equation = value.equation()
        if maybe_equation:
            print(Equation(self.variables, maybe_equation).value)
            return

    # Exit a parse tree produced by Wuwuzela_GrammarParser#printStatement.
    def exitPrintStatement(self, ctx:Wuwuzela_GrammarParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#value.
    def enterValue(self, ctx:Wuwuzela_GrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#value.
    def exitValue(self, ctx:Wuwuzela_GrammarParser.ValueContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#ifStatement.
    def enterIfStatement(self, ctx:Wuwuzela_GrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#ifStatement.
    def exitIfStatement(self, ctx:Wuwuzela_GrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#varStatement.
    def enterVarStatement(self, ctx:Wuwuzela_GrammarParser.VarStatementContext):
        self.variables.new(str(ctx.VARIABLE()), ctx.varStatementContent())

    # Exit a parse tree produced by Wuwuzela_GrammarParser#varStatement.
    def exitVarStatement(self, ctx:Wuwuzela_GrammarParser.VarStatementContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#varStatementContent.
    def enterVarStatementContent(self, ctx:Wuwuzela_GrammarParser.VarStatementContentContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#varStatementContent.
    def exitVarStatementContent(self, ctx:Wuwuzela_GrammarParser.VarStatementContentContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#containerStatement.
    def enterContainerStatement(self, ctx:Wuwuzela_GrammarParser.ContainerStatementContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#containerStatement.
    def exitContainerStatement(self, ctx:Wuwuzela_GrammarParser.ContainerStatementContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#containerContent.
    def enterContainerContent(self, ctx:Wuwuzela_GrammarParser.ContainerContentContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#containerContent.
    def exitContainerContent(self, ctx:Wuwuzela_GrammarParser.ContainerContentContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#transposeStatement.
    def enterTransposeStatement(self, ctx:Wuwuzela_GrammarParser.TransposeStatementContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#transposeStatement.
    def exitTransposeStatement(self, ctx:Wuwuzela_GrammarParser.TransposeStatementContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#compositionStatement.
    def enterCompositionStatement(self, ctx:Wuwuzela_GrammarParser.CompositionStatementContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#compositionStatement.
    def exitCompositionStatement(self, ctx:Wuwuzela_GrammarParser.CompositionStatementContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#write.
    def enterWrite(self, ctx:Wuwuzela_GrammarParser.WriteContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#write.
    def exitWrite(self, ctx:Wuwuzela_GrammarParser.WriteContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#logicalExpression.
    def enterLogicalExpression(self, ctx:Wuwuzela_GrammarParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#logicalExpression.
    def exitLogicalExpression(self, ctx:Wuwuzela_GrammarParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#andOr.
    def enterAndOr(self, ctx:Wuwuzela_GrammarParser.AndOrContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#andOr.
    def exitAndOr(self, ctx:Wuwuzela_GrammarParser.AndOrContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#comparison.
    def enterComparison(self, ctx:Wuwuzela_GrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#comparison.
    def exitComparison(self, ctx:Wuwuzela_GrammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#equation.
    def enterEquation(self, ctx:Wuwuzela_GrammarParser.EquationContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#equation.
    def exitEquation(self, ctx:Wuwuzela_GrammarParser.EquationContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#element.
    def enterElement(self, ctx:Wuwuzela_GrammarParser.ElementContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#element.
    def exitElement(self, ctx:Wuwuzela_GrammarParser.ElementContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#mathOperation.
    def enterMathOperation(self, ctx:Wuwuzela_GrammarParser.MathOperationContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#mathOperation.
    def exitMathOperation(self, ctx:Wuwuzela_GrammarParser.MathOperationContext):
        pass


    # Enter a parse tree produced by Wuwuzela_GrammarParser#trueFalse.
    def enterTrueFalse(self, ctx:Wuwuzela_GrammarParser.TrueFalseContext):
        pass

    # Exit a parse tree produced by Wuwuzela_GrammarParser#trueFalse.
    def exitTrueFalse(self, ctx:Wuwuzela_GrammarParser.TrueFalseContext):
        pass