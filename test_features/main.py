import sys
from interpreter import*
from lexer import Lexer
from parser import Parser
from fun_parser import Fun_Parser
def runFile(file_path):
    with open(file_path,'r') as file:
        source = file.read()
        lexer = Lexer(source)
        lexer.scan()
        parser = Parser(lexer.tokens)
        fun_parser = Fun_Parser(lexer.tokens)
        parser.parse()
        fun_parser.parse()
        interpreter = Interpreter()
        interpreter.interpret(fun_parser.statement)
        interpreter.interpret(parser.statement)


if __name__ == '__main__':
    debug_mode =  True
    if debug_mode == True:
        file_path = "test.ora"
        runFile(file_path)
    else:
        if len(sys.argv)<2:
            print("correct usage python main.py [input file].ora")
            exit()
        file_path = sys.argv[1]
        runFile(file_path)


