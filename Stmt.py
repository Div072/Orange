from __future__ import annotations
from Expr import Expr

from abc import ABC, abstractmethod
from token_ import Token

class Visitor(ABC):
    @abstractmethod
    def visitPrintStmt(self,stmt: Print)->None:
        pass
    @abstractmethod
    def visitExpressionStmt(self, stmt:Expression)->None:
        pass

class Stmt(ABC):
    def accept(self,visitor:Visitor)->None:
        pass
class Print(Stmt):
    def __init__(self,expression:Expr):
        self.expression = expression

    def accept(self,visitor:Visitor):
        return visitor.visitPrintStmt(self)
class Expression(Stmt):
    def __init__(self,expression:Expr):
        self.expression = expression
    def accept(self,visitor:Visitor):
        return visitor.visitExpressionStmt(self)