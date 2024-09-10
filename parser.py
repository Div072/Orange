from unittest.mock import right

import Expr
from Expr import *
from token_ import *
from Stmt import *
# I'm using Visitor Pattern to keep this code clean
class Parser:
    def __init__(self,tokens:[]):
        self.tokens = tokens
        self.curr = 0
        self.statement = []

    def parse(self):
        while self.peek().type != Tokentype.EOF and self.curr< len(self.tokens):
            self.statement.append(self.declaration())
    def declaration(self):
        if self.peek().type == Tokentype.VAR:
            self.advance() #consume var
            return self.varDeclaration()
        else:
            return self.stmt()
    def varDeclaration(self):
        tok = None
        if self.peek().type == Tokentype.INDENT:
            tok = self.peek()
            self.advance()
        else:
            print("Expect variable name")
            exit()
        exp = None
        if self.peek().type == Tokentype.EQUAL:
            self.advance()
            exp = self.expression()
        if self.peek().type != Tokentype.SEMICOLON:
            print("Expect ; after statement and declaration")
            exit()
        self.advance()
        return Var(tok,exp)

    def stmt(self):
        if self.peek().type == Tokentype.PRINT:
            self.advance()
            if self.peek().type != Tokentype.OPENBRA:
                print("correct syntax print(expression)")
                exit()
            self.advance() #consume (
            return self.printStatement()
        else:
            return self.expressionStmt()
    def printStatement(self):
        expr = self.expression()
        if self.peek().type != Tokentype.CLOSEBRA:
            print("correct syntax print(expression)")
            exit()
        self.advance() #consume )
        return Print(expr)

    def expressionStmt(self):
        expr = self.expression()
        if self.peek().type != Tokentype.SEMICOLON:
            print("require ; in the end of epxression statement")
            exit()
        self.advance() #consume ;
        return Expression(expr)

    def expression(self):
        return self.assignMent()

    def assignMent(self):
        expr = self.equality()
        if self.peek().type == Tokentype.EQUAL:
            self.advance()
            tok = self.peek_previous()
            val = self.assignMent()
            if isinstance(expr,Variable):
                name = expr.name
                return Assign(name,val)
            else:
                print(tok,"Invalid assignment targe")
                exit()
        return expr
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
        left = self.logical()
        while self.peek().type == Tokentype.MULTIPLY or self.peek().type==Tokentype.DIVIDE:
            self.advance()
            operator = self.peek_previous()

            right = self.logical()
            left = Binary(left,operator,right)
        return left
    def logical(self):
        # a && b
        left = self.unary()
        while self.peek().type == Tokentype.AND or self.peek().type == Tokentype.OR:
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
        if token.type == Tokentype.FALSE:
            self.advance()
            return Literal(token.lexeme)
        if token.type == Tokentype.TRUE:
            self.advance()
            return Literal(token.lexeme)
        if token.type == Tokentype.INDENT:
            self.advance()
            return Variable(token.lexeme)
        if token.type == Tokentype.OPENBRA:
            self.advance()
            expr = self.equality()
            if self.peek().type != Tokentype.CLOSEBRA:
                print("missing close ) token")
                exit()
            self.advance() #consume )
            return Grouping(expr)


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




