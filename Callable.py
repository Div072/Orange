
from Env import Environment
from Stmt import Stmt, FunDec

class Fun_callable():
    def __init__(self,fun_stmt:FunDec):
        self.declaration = fun_stmt

    def call(self,interpreter,arguments:[]):
        environment = Environment(interpreter.global_)
        for i in range(len(self.declaration.parameters)):
            environment.initiate(self.declaration.parameters[i].name,arguments[i])
        interpreter.executeBlock(self.declaration.fun_block.statements,environment)
        return