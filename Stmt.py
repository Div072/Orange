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
    @abstractmethod
    def visitVarStmt(self,stmt:Var)->None:
        pass
    @abstractmethod
    def visitBlockStmt(self,stmt:Block)->None:
        pass
    @abstractmethod
    def visitIFStmt(self,stmt:IF_Stmt)->None:
        pass
    @abstractmethod
    def visitWhileStmt(self,stmt:WHile)->None:
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
class Var(Stmt):
    def __init__(self,name:Token,expr:Expr):
        self.name = name
        self.intializer = expr

    def accept(self,visitor:Visitor):
        return visitor.visitVarStmt(self)
class Block(Stmt):
    def __init__(self,statements):
        self.statements = statements
    def accept(self,visitor:Visitor):
        return visitor.visitBlockStmt(self)
class IF_Stmt(Stmt):
    def __init__(self,IF,expr:Expr,EL:Stmt = None,ELIF:Stmt = None):
        self.IF = IF
        self.expr = expr
        self.EL = EL
        self.ELIF = ELIF
    def accept(self,visitor:Visitor):
        return visitor.visitIFStmt(self)
class WHile(Stmt):
    def __init__(self,expr:Expr,WH:Stmt=None):
        self.expr = expr
        self.WH = WH
    def accept(self,visitor:Visitor):
        return visitor.visitWhileStmt(self)

