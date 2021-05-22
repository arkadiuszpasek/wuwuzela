import sys
from antlr4 import *
from Wuwuzela_GrammarLexer import Wuwuzela_GrammarLexer
from Wuwuzela_GrammarParser import Wuwuzela_GrammarParser

def main(argv):
    input = FileStream(argv[1])
    lexer = Wuwuzela_GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Wuwuzela_GrammarParser(stream)
    tree = parser.musicProgram()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)