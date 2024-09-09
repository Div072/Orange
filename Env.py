from wsgiref.validate import validator

from token_ import*
class Environment:
    def __init__(self):
        self.values = {}
    def initiate(self,name,value):
        self.values[name] = value
    def get(self,name:Token):
        if self.values.get(name.lexeme,False):
            return self.values.get(name.lexeme)
        else:
            print("Undefined variable: ",name.lexeme)
            exit()

