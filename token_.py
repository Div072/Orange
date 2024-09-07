from enum import Enum, auto

class Tokentype(Enum):
    SEMICOLON = auto()
    NUMBER = auto()
    PRINT = auto()
    INDENT = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    EQUAL = auto()
    BANG = auto()
    BANG_EQUAL = auto()
    EQUAL_EQUAL= auto()
    GREATER= auto()
    LESS = auto()
    GREATER_EQUAL = auto()
    LESS_EQUAL= auto()
    STRING = auto()
    VAR = auto()
    WHILE = auto()
    FOR = auto()
    FUN = auto()

    EOF = auto()


class Token:
    def __init__(self, tokentype, lexeme, line):
        self.type = tokentype
        self.lexeme = lexeme
        self.line = line


    def addToken(tokentype, lexeme, line):
        return Token(tokentype, lexeme, line)
