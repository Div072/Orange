from Expr import*

from parser import Parser
from token_ import Tokentype


# we are applying visitor pattern for Interpreter also

class Interpreter(Visitor):

    def eval(self,expr):
        return expr.accept(self)
    def visitBinnaryExpr(self,expr:Binary):
        left=self.eval(expr.left)
        right = self.eval(expr.right)
        match expr.operator:
            case Tokentype.PLUS:
                return int( left) + int( right)
            case Tokentype.MINUS:
                return int( left) - int( right)
            case Tokentype.MULTIPLY:
                return int( left) * int( right)
            case Tokentype.DIVIDE:
                return int( left) / int(right)
            case Tokentype.LESS:
                return int(left)<int(right)
            case Tokentype.GREATER:
                return int(left)>int(right)
            case Tokentype.LESS_EQUAL:
                return int(left)<=int(right)
            case Tokentype.GREATER_EQUAL:
                return int(left)>=int(right)
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
           print(value)

