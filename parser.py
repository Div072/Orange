from lexer import Lexer
from Expr import *
from token_ import *

class Parser:
    def __init__(self,tokens:[]):
        self.tokens = tokens
        self.curr = 0
        self.statement = []
        #Lexer.tokens = None

    def parse(self):
        while self.peek().type != Tokentype.EOF and self.curr< len(self.tokens):
            self.statement.append(self.term())

    def term(self):
        left =  self.factor() #change it after to unary
        while self.peek().type == Tokentype.PLUS or self.peek().type == Tokentype.MINUS:
            self.advance()
            operator = self.peek_previous()
            print("plus")
            right = self.factor() #change it after creating calss to unary
            left = Binary(left,operator,right)
        return left
            # TODO implement class for binary
    def factor(self):
        left = self.unary()
        while self.peek().type == Tokentype.MULTIPLY or self.peek().type==Tokentype.DIVIDE:
            self.advance()
            operator = self.peek_previous()
            print("multiply")
            right = self.unary()
            left = Binary(left,operator,right)
        return left
    def unary(self):
        if self.peek().type == Tokentype.BANG or self.peek().type == Tokentype.MINUS:
            self.advance()
            operator = self.peek_previous()
            print("Unary")
            right = self.unary()
            return Unary(operator,right)

        else:
            return self.primary()
    def primary(self):
        token = self.peek()

        if self.peek().type == Tokentype.NUMBER:
            self.advance()
            print("number")
            return Literal(token.lexeme)
        if token.type == Tokentype.STRING:
            return Literal(token.lexeme)
        if token.type == Tokentype.EOF:
            return
        print("Unexpected token",token.type)
        exit()


    def peek(self):
        # be aware this peek method is also increasing curr pointer by one
        if self.curr<len(self.tokens):
            return self.tokens[self.curr]
        return Token(Tokentype.EOF,"EOF",0)
    def advance(self):
        if self.IsEnd():
            return False
        self.curr +=1
        return True
    def IsEnd(self):
        if self.curr>= len(self.tokens) or self.peek()==Tokentype.EOF:
            return True
        return False
    def peek_previous(self):
        if self.curr-1>=0:
            return self.tokens[self.curr-1]
        else:
            print("peek_previous() acessing index less than 0")
            exit()




