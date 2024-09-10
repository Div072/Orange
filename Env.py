
from token_ import*
class Environment:
    def __init__(self):
        self.values = {}
    def initiate(self,name,value):
        self.values[name] = value
    def get(self,name):
        #it accepts string
        if name in self.values:
            return self.values.get(name)
        else:
            print("Undefined variable from get method: ",name)
            exit()

    def assign(self,name:Token,value):
        if name in self.values:
            self.values[name] = value
            return
        else:
            print("Undefined variable from assign: ",name.lexeme)
            exit()

