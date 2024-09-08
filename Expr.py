from __future__ import annotations
from abc import ABC, abstractmethod
from token_ import Token
class Visitor(ABC):
    @abstractmethod
    def visitBinnaryExpr(self,expr:Binary)->None:
        pass
    @abstractmethod
    def visitLiteralExpr(self,expr:Literal)->None:
        pass
    @abstractmethod
    def visitUnaryExpr(self,expr: Unary)->None:
        pass

class Expr(ABC):
    def accept(self,visitor:Visitor)-> None:
        pass

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
        self.rigt = right
    def accept(self,visitor:Visitor):
        return visitor.visitUnaryExpr(self)

class Literal(Expr):
    def __init__(self, value):
        self.value = value
    def accept(self,visitor:Visitor):
        return visitor.visitLiteralExpr(self)
