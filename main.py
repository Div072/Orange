import sys
from interpreter import Interpreter
from lexer import Lexer
from parser import Parser
def runFile(file_path):
    with open(file_path,'r') as file:
        source = file.read()
        lexer = Lexer(source)
        lexer.scan()
        parser = Parser(lexer.tokens)
        parser.parse()
        interpreter = Interpreter()
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


