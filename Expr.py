from __future__ import annotations
from abc import ABC, abstractmethod
from token_ import Token
class Visitor(ABC):
    @abstractmethod
    def visitAssignExpr(self,expr:Assign)->None:
        pass
    @abstractmethod
    def visitBinnaryExpr(self,expr:Binary)->None:
        pass
    @abstractmethod
    def visitLiteralExpr(self,expr:Literal)->None:
        pass
    @abstractmethod
    def visitUnaryExpr(self,expr: Unary)->None:
        pass
    @abstractmethod
    def visitGroupingExpr(self,expr:Grouping)->None:
        pass
    @abstractmethod
    def visitVariableExpr(self, expr:Variable)->None:
        pass
    @abstractmethod
    def visitCallExpr(self,expr:Call)->None:
        pass

class Expr(ABC):
    def accept(self,visitor:Visitor)-> None:
        pass
class Assign(Expr):
    def __init__(self,name:Token,value:Expr):
        self.name = name
        self.value = value
    def accept(self,visitor:Visitor):
        return visitor.visitAssignExpr(self)

class Binary(Expr):
    def __init__(self,left:Expr,token:Token,right:Expr):
        self.left = left
        self.operator = token.type
        self.right = right
    def accept(self,visitor:Visitor):
        return visitor.visitBinnaryExpr(self)

class Unary(Expr):
    def __init__(self,token:Token,right:Expr):
        self.operand = token.type
        self.right = right
    def accept(self,visitor:Visitor):
        return visitor.visitUnaryExpr(self)

class Grouping(Expr):
    def __init__(self,expression:Expr):
        self.expression = expression
    def accept(self,visitor:Visitor):
        return visitor.visitGroupingExpr(self)

class Literal(Expr):
    def __init__(self, value):
        self.value = value
    def accept(self,visitor:Visitor):
        return visitor.visitLiteralExpr(self)
class Variable(Expr):
    def __init__(self,name):
        self.name = name
    def accept(self,visitor:Visitor):
        return visitor.visitVariableExpr(self)

class Call(Expr):
    def __init__(self,callee:Expr,paren:Token,arguments:[]):
        self.callee = callee
        self.paren = paren
        self.arguments = arguments
    def accept(self,visitor:Visitor):
        return visitor.visitCallExpr(self)






