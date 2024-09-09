from Expr import*
from Stmt import*
from token_ import Tokentype
from Env import Environment

# we are applying visitor pattern for Interpreter also

class Interpreter(Visitor):
    def __init__(self):
        self.environment = Environment()
    def eval(self,expr):
        return expr.accept(self)
    def visitVarStmt(self,stmt:Var):
        value = None
        if stmt.intializer:
            value = self.eval(stmt.intializer)
        Environment.initiate(self.environment,stmt.name.lexeme,value)
        return

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


