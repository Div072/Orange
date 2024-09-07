import sys
from lexer import Lexer

def runFile(file_path):
    with open(file_path,'r') as file:
        source = file.read()
        lexer = Lexer(source)
        lexer.scan()
        for i in lexer.tokens:
            print(i.lexeme)

if __name__ == '__main__':
    debug_mode =  False
    if debug_mode == True:
        file_path = "test.ora"
        runFile(file_path)
    else:
        if len(sys.argv)<2:
            print("correct usage python main.py [input file].ora")
            exit()
        file_path = sys.argv[1]
        runFile(file_path)

