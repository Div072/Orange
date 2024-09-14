from Stmt import FunDec
from token_ import*
class Environment:
    def __init__(self,env= None,fun_env=None):
        self.values = {}
        self.env = env #parent node variable env
        self.fun_obj = {} #list of all
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
        if self.env != None:
            self.env.assign(name,value)
            return
        print("Undefined variable from assign: ",name)
        exit()
    """
    TODO: find a better way to get_fun then use recur fun 
    def intialize_fun(self,fun_stmt:FunDec):
        self.fun_obj[fun_stmt.name.name] = fun_stmt
        return

    def get_fun(self,name):
        if name in self.fun_obj:
            return self.fun_obj[name]
        if self.env!=None:
            return self.env.get_fun(name)

        print("Undeclared function:", name)
        exit() 
    """
