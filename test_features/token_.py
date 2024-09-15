from enum import Enum, auto

class Tokentype(Enum):
    SEMICOLON = auto()
    COMA = auto()
    NUMBER = auto()
    PRINT = auto()
    INDENT = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    EQUAL = auto()
    BANG = auto()
    OR =  auto()
    AND = auto()
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
    IF = auto()
    ELSE = auto()
    DO = auto()
    ELIF = auto()
    FUN = auto()
    OPENBRA = auto()
    CLOSEBRA =  auto()
    OPENPARA = auto()
    CLOSEPARA = auto()
    TRUE = auto()
    FALSE = auto()
    EOF = auto()

class Token:
    def __init__(self, tokentype, lexeme, line):
        self.type = tokentype
        self.lexeme = lexeme
        self.line = line

    def addToken(tokentype, lexeme, line):
        return Token(tokentype, lexeme, line)
