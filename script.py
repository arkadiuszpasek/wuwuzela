import sys
from antlr4 import *
from grammar.Wuwuzela_GrammarLexer import Wuwuzela_GrammarLexer
from grammar.Wuwuzela_GrammarParser import Wuwuzela_GrammarParser
from src.WuwuzelaListener import WuwuzelaListener

def main(argv):
    input = FileStream(argv[1])
    lexer = Wuwuzela_GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Wuwuzela_GrammarParser(stream)
    tree = parser.musicProgram()

    listener = WuwuzelaListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)