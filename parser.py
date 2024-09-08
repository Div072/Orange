from lexer import Lexer
from Expr import *
from token_ import *
# I'm using Visitor Pattern to keep this code clean
class Parser:
    def __init__(self,tokens:[]):
        self.tokens = tokens
        self.curr = 0
        self.statement = []
        #Lexer.tokens = None

    def parse(self):
        while self.peek().type != Tokentype.EOF and self.curr< len(self.tokens):
            self.statement.append(self.equality())
    def equality(self):
        left = self.comparision()
        while self.peek().type == Tokentype.BANG_EQUAL or self.peek().type == Tokentype.EQUAL_EQUAL:
            self.advance()
            operand = self.peek_previous()
            right = self.comparision()
            left = Binary(left,operand,right)
        return left
    def comparision(self):
        left = self.term()
        while self.peek().type == Tokentype.GREATER_EQUAL or self.peek().type == Tokentype.GREATER_EQUAL or self.peek().type == Tokentype.LESS_EQUAL or self.peek().type == Tokentype.LESS:
            self.advance()
            operand = self.peek_previous()
            right = self.term()
            left = Binary(left,operand,right)
        return left

    def term(self):
        left =  self.factor()
        while self.peek().type == Tokentype.PLUS or self.peek().type == Tokentype.MINUS:
            self.advance()
            operator = self.peek_previous()

            right = self.factor()
            left = Binary(left,operator,right)
        return left

    def factor(self):
        print(self.curr)
        left = self.unary()
        while self.peek().type == Tokentype.MULTIPLY or self.peek().type==Tokentype.DIVIDE:
            self.advance()
            operator = self.peek_previous()

            right = self.unary()
            left = Binary(left,operator,right)
        return left
    def unary(self):
        if self.peek().type == Tokentype.BANG or self.peek().type == Tokentype.MINUS:
            self.advance()
            operator = self.peek_previous()

            right = self.unary()
            return Unary(operator,right)

        else:
            return self.primary()
    def primary(self):
        token = self.peek()
        if self.peek().type == Tokentype.NUMBER:
            self.advance()
            return Literal(token.lexeme)
        if token.type == Tokentype.STRING:
            self.advance()
            return Literal(token.lexeme)

        if token.type == Tokentype.OPENBRA:
            self.advance()
            expr = self.equality()
            if self.peek().type != Tokentype.CLOSEBRA:
                print("missing close ) token")
                exit()
            self.advance() #consume )
            return Grouping(expr)
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




