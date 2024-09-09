from sys import exec_prefix
from turtledemo.penrose import start

from Expr import*
from Stmt import*
from parser import Parser
from token_ import Tokentype


# we are applying visitor pattern for Interpreter also

class Interpreter(Visitor):

    def eval(self,expr):
        return expr.accept(self)
    def visitPrintStmt(self,stmt:Print):
        expr = self.eval(stmt.expression)
        print(expr)
    def visitExpressionStmt(self, stmt:Expression):
        return self.eval(stmt.expression)

    def visitBinnaryExpr(self,expr:Binary):
        left=self.eval(expr.left)
        right = self.eval(expr.right)
        match expr.operator:
            case Tokentype.PLUS:
                return left +  right
            case Tokentype.MINUS:
                return left - right
            case Tokentype.MULTIPLY:
                return left * right
            case Tokentype.DIVIDE:
                return left / right
            case Tokentype.LESS:
                return left < right
            case Tokentype.GREATER:
                return left > right
            case Tokentype.LESS_EQUAL:
                return left<=right
            case Tokentype.GREATER_EQUAL:
                return left>=right
            case _:
                print("for binary expression got invalid operator")
                exit()
    def visitLiteralExpr(self,expr:Literal):
        return expr.value
    def visitUnaryExpr(self,expr: Unary):
        right = self.eval(expr.right)
        match expr.operand:
            case Tokentype.MINUS:
                return -int(right)
            case Tokentype.BANG:
                return not right
            case _:
                print("for unary expression got invalid operator")
                exit()
    def visitGroupingExpr(self,expr:Grouping):
        return self.eval(expr.expression)

    def interpret(self,statements:[]):
        for statement in statements:
           value =  self.eval(statement)


