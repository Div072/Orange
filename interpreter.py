from collections.abc import Callable

from Expr import*
from Stmt import*
from token_ import Tokentype
from Env import Environment
from Callable import Fun_callable


# we are applying visitor pattern for Interpreter also
class Interpreter(Visitor):
    def __init__(self):
        self.global_ = Environment()
        self.environment = self.global_
    def eval(self,expr):
        return expr.accept(self)

    def visitAssignExpr(self,expr:Assign):
        value = self.eval(expr.value)
        Environment.assign(self.environment,expr.name,value)
        return value

    def visitVarStmt(self,stmt:Var):
        value = None
        if stmt.intializer:
            value = self.eval(stmt.intializer)
        Environment.initiate(self.environment,stmt.name.lexeme,value)
        return
    def visitFunDeclarationStmt(self,stmt:FunDec):
        function_ = Fun_callable(stmt)
        self.environment.initiate(stmt.name,function_)
        return

    def visitPrintStmt(self,stmt:Print):
        expr = self.eval(stmt.expression)
        print(expr)
    def visitExpressionStmt(self, stmt:Expression):
        return self.eval(stmt.expression)
    def visitIFStmt(self,stmt:IF_Stmt):
        return self.executeIF(stmt.IF,stmt.expr,stmt.EL)
    def visitBlockStmt(self,stmt:Block):
        return self.executeBlock(stmt.statements, Environment(self.environment))

    def visitWhileStmt(self,stmt:WHile):
        while  self.IsTrue(self.eval(stmt.expr)):
             self.executeWhile(stmt.expr,stmt.WH)
    def executeWhile(self,expr:Expr,Wh:Block):
        self.executeBlock(Wh.statements, Environment(self.environment))

    def executeIF(self,If_block:Block,expr:Expr,El_blcok:Block = None):
        decision_expr = None
        if expr !=None:
            decision_expr = self.eval(expr)
        else:
            print("Error from Interpreter: expression of if cannot be none",)
        if self.IsTrue(decision_expr):
            self.executeBlock(If_block.statements,Environment(self.environment))
        elif El_blcok!=None:
            self.executeBlock(El_blcok.statements,Environment(self.environment))
    def executeBlock(self,statements,env):
        prv = self.environment
        try:
            self.environment = env
            for statement in statements:
                self.eval(statement)
        finally:
            self.environment = prv

    def visitVariableExpr(self, expr: Variable):
        return self.environment.get(expr.name)

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
            case Tokentype.EQUAL_EQUAL:
                return left == right
            case Tokentype.OR:
                return self.IsTrue(left) or self.IsTrue(right)
            case Tokentype.AND:
                return  self.IsTrue(left) and self.IsTrue(right)
            case _:
                print("for binary expression got invalid operator",expr.operator)
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
    def visitCallExpr(self,expr:Call):
        callee = self.eval(expr.callee) # return Fun_callable object
        arguments = []
        for argument in expr.arguments:
            arguments.append(self.eval(argument))# append literals
        callee.call(self,arguments)

    def visitGroupingExpr(self,expr:Grouping):
        return self.eval(expr.expression)

    def interpret(self,statements:[]):
        for statement in statements:
           value =  self.eval(statement)


    def IsTrue(self,val):
        if isinstance(val,bool):
            return val
        elif val != None:
            return True
        return False