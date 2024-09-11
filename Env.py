
from token_ import*
class Environment:
    def __init__(self,env= None):
        self.values = {}
        self.env = env #parent env
        #be careful because you cannot just tell python to create instance of his own type

    def initiate(self,name,value):
        self.values[name] = value
    def get(self,name):
        #it accepts string
        if name in self.values:
            return self.values.get(name)
        if self.env !=None:
            return self.env.get(name)

        print("Undefined variable from get method: ",name)
        exit()

    def assign(self,name:Token,value):
        if name in self.values:
            self.values[name] = value
            return
        if self.env!=None:
            self.env.assign(name,value)
            return
        print("Undefined variable from assign: ",name)
        exit()

