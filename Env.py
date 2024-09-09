from wsgiref.validate import validator

from token_ import*
class Environment:
    def __init__(self):
        self.values = {}
    def initiate(self,name,value):
        self.values[name] = value
    def get(self,name):
        #it accepts string
        if self.values.get(name,False):
            return self.values.get(name)
        else:
            print("Undefined variable: ",name)
            exit()

    def assign(self,name:Token,value):
        if self.values.get(name,False):
            self.values[name] = value
            return
        else:
            print("Undefined variable: ",name.lexeme)
            exit()

