from token_ import Tokentype
from Expr import*
from Stmt import*
class Fun_Parser:
    def __init__(self,tokens:[]):
        self.tokens = tokens
        self.curr = 0
        self.statement = []
    def parse(self):
        while self.peek().type != Tokentype.EOF and self.curr < len(self.tokens):
            if self.peek().type == Tokentype.FUN:

                self.statement.append(self.fun_parse())
            else:
                self.advance()

    def fun_parse(self):
        if self.peek().type == Tokentype.FUN:
            self.advance() #consume fun keyword
            return self.fun_declaration()
        else:
            self.advance()

    def declaration(self):
        if self.peek().type == Tokentype.VAR:
            self.advance()  # consume var
            return self.varDeclaration()
        else:
            return self.stmt()

    def varDeclaration(self):
        tok = None
        if self.peek().type == Tokentype.INDENT:
            tok = self.peek()
            self.advance()  # consume token Indent
        else:
            print("Error from parser: Expect variable name: ")
            exit()
        exp = None
        if self.peek().type == Tokentype.EQUAL:
            self.advance()  # consume token equal
            exp = self.expression()
        if self.peek().type != Tokentype.SEMICOLON:
            print("Error from parser: Expect ; after statement and declaration")
            exit()
        self.advance()  # consume token semicolon
        return Var(tok, exp)

    def stmt(self):
        if self.peek().type == Tokentype.PRINT:
            self.advance()  # consume token print
            if self.peek().type != Tokentype.OPENBRA:
                print("Error from parser: correct syntax print(expression): ")
                exit()
            self.advance()  # consume (
            return self.printStatement()
        elif self.peek().type == Tokentype.IF:
            return self.ifStatement()
        elif self.peek().type == Tokentype.WHILE:
            return self.whileStatement()
        elif self.peek().type == Tokentype.OPENPARA:
            self.advance()  # consume token Openpara
            return Block(self.block())
        else:
            return self.expressionStmt()

    def fun_declaration(self):
        calleee = self.primary()  # will return variable Indent
        parameters = []
        if self.peek().type == Tokentype.OPENBRA:
            self.advance()  # consume (
            if self.peek().type != Tokentype.CLOSEBRA:
                while True:
                    parameters.append(self.expression())
                    if self.peek().type != Tokentype.COMA:
                        break
                    else:
                        self.advance()  # consume ,
            if self.peek().type != Tokentype.CLOSEBRA:
                print("Error from parser: missing ) in function declaration")
                exit()
            else:
                self.advance()  # consume )
                if self.peek().type == Tokentype.OPENPARA:
                    self.advance()  # consume {
                    fun_block = Block(self.block())
                    return FunDec(calleee.name, parameters, fun_block)
                else:
                    print("Error from parser: missing { in function declaration")
                    exit()
        else:
            print("Error from parser: missing ( in function declaration")
            exit()

    def printStatement(self):
        expr = self.expression()
        if self.peek().type != Tokentype.CLOSEBRA:
            print("Error from parser: correct syntax print(expression)")
            exit()
        self.advance()  # consume )
        return Print(expr)

    def ifStatement(self):
        self.advance()  # consume if
        expr = self.expression()
        IF_statment = None
        El_statment = None
        if self.peek().type == Tokentype.OPENPARA:
            self.advance()
            IF_statment = Block(self.block())  # block will take care of }
            if self.peek().type == Tokentype.ELSE:
                self.advance()  # consume else
                if self.peek().type == Tokentype.OPENPARA:
                    self.advance()  # consume {
                    El_statment = Block(self.block())
            return IF_Stmt(IF_statment, expr, El_statment)
        else:
            print("Error from parser: missing {: ")
            exit()

    def whileStatement(self):
        self.advance()  # consume while token
        expr = self.expression()
        Wh = None
        if self.peek().type == Tokentype.OPENPARA:
            self.advance()  # consume {
            Wh = Block(self.block())
            return WHile(expr, Wh)
        else:
            print("Error from parser: missing {")
            exit()
        pass

    def expressionStmt(self):
        expr = self.expression()
        if self.peek().type != Tokentype.SEMICOLON:
            print("require ; in the end of epxression statement")
            exit()
        self.advance()  # consume ;
        return Expression(expr)

    def block(self):
        statements = []
        while self.peek().type != Tokentype.CLOSEPARA and not self.IsEnd():
            statements.append(self.declaration())
        if self.peek().type != Tokentype.CLOSEPARA:
            print("expect '}' after block")
            exit()
        self.advance()  # consume '}'
        return statements

    def expression(self):
        return self.assignMent()

    """ Logical operators are different than usual binary operators 
    expression->assingment
    assingment-> IDENTIFIER "=" assingment | logical_or
    logical_or -> logical_and ("or" logical_and)*;
    logical_and -> equality ("and" equality)*;
    """

    def assignMent(self):
        expr = self.logical_or()
        if self.peek().type == Tokentype.EQUAL:
            self.advance()
            tok = self.peek_previous()
            val = self.assignMent()
            if isinstance(expr, Variable):
                name = expr.name
                return Assign(name, val)
            else:
                print(tok, "Error from parser: Invalid assignment targe")
                exit()
        return expr

    def logical_or(self):
        left = self.logical_and()
        while self.peek().type == Tokentype.OR:
            self.advance()
            operator = self.peek_previous()
            right = self.logical_and()
            left = Binary(left, operator, right)
        return left

    def logical_and(self):
        left = self.equality()
        while self.peek().type == Tokentype.AND:
            self.advance()
            operator = self.peek_previous()
            right = self.equality()
            left = Binary(left, operator, right)
        return left

    def equality(self):
        left = self.comparision()
        while self.peek().type == Tokentype.BANG_EQUAL or self.peek().type == Tokentype.EQUAL_EQUAL:
            self.advance()
            operand = self.peek_previous()
            right = self.comparision()
            left = Binary(left, operand, right)
        return left

    def comparision(self):
        left = self.term()
        while self.peek().type == Tokentype.GREATER_EQUAL or self.peek().type == Tokentype.GREATER or self.peek().type == Tokentype.LESS_EQUAL or self.peek().type == Tokentype.LESS:
            self.advance()
            operand = self.peek_previous()
            right = self.term()
            left = Binary(left, operand, right)
        return left

    def term(self):
        left = self.factor()
        while self.peek().type == Tokentype.PLUS or self.peek().type == Tokentype.MINUS:
            self.advance()
            operator = self.peek_previous()

            right = self.factor()
            left = Binary(left, operator, right)
        return left

    def factor(self):
        left = self.unary()
        while self.peek().type == Tokentype.MULTIPLY or self.peek().type == Tokentype.DIVIDE:
            self.advance()
            operator = self.peek_previous()

            right = self.unary()
            left = Binary(left, operator, right)
        return left

    def unary(self):
        if self.peek().type == Tokentype.BANG or self.peek().type == Tokentype.MINUS:
            self.advance()
            operator = self.peek_previous()

            right = self.unary()
            return Unary(operator, right)

        else:
            return self.call_call()

    """ function calls have higher precedence than any other operator 
    rule: unary -> (! | -) unary | call               
    call -> primary (( arguments ?))*
    arguments -> expression ("," expression)*;
    """

    def call_call(self):
        expr = self.primary()  # will return variable type class
        while True:
            if self.peek().type == Tokentype.OPENBRA:
                self.advance()  # consume {
                expr = self.call_helper(expr)
            else:
                break
        return expr

    def primary(self):
        token = self.peek()
        if self.peek().type == Tokentype.NUMBER:
            self.advance()
            return Literal(token.lexeme)
        if token.type == Tokentype.STRING:
            self.advance()
            return Literal(token.lexeme)
        if token.type == Tokentype.FALSE:
            self.advance()
            return Literal(token.lexeme)
        if token.type == Tokentype.TRUE:
            self.advance()
            return Literal(token.lexeme)
        if token.type == Tokentype.INDENT:
            self.advance()
            return Variable(token.lexeme)
        if token.type == Tokentype.OPENBRA:
            self.advance()
            expr = self.equality()
            if self.peek().type != Tokentype.CLOSEBRA:
                print("Error from parser: missing close ) token")
                exit()
            self.advance()  # consume )
            return Grouping(expr)

    def call_helper(self, expr: Expr):
        arguments = []
        if self.peek().type != Tokentype.CLOSEBRA:
            while True:
                arguments.append(self.expression())
                if self.peek().type == Tokentype.COMA:
                    self.advance()  # consume ,
                else:
                    break
        paren = self.consume(Tokentype.CLOSEBRA, "Error from parser: Mising ) in call_call")
        return Call(expr, paren, arguments)

    def peek(self):
        # be aware this peek method is also increasing curr pointer by one
        if self.curr < len(self.tokens):
            return self.tokens[self.curr]
        return Token(Tokentype.EOF, "EOF", 0)

    def advance(self):
        if self.IsEnd():
            return False
        self.curr += 1
        return True

    def IsEnd(self):
        if self.curr >= len(self.tokens) or self.peek() == Tokentype.EOF:
            return True
        return False

    def peek_previous(self):
        if self.curr - 1 >= 0:
            return self.tokens[self.curr - 1]
        else:
            print("pError from parser: peek_previous() acessing index less than 0")
            exit()

    def consume(self, token_type: Tokentype, message):
        if self.peek().type != token_type:
            print(message)
            exit()
        else:
            self.advance()
            return self.peek_previous()