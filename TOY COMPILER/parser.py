from rply import ParserGenerator
from ast_nodes import Number, BinaryOp, Assignment, Print, Identifier

class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['NUMBER', 'ID', 'PLUS', 'MINUS', 'MUL', 'DIV', 'ASSIGN', 'PRINT', 'LPAREN', 'RPAREN'],
            precedence=[
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV'])
            ]
        )
        self._define_rules()

    def _define_rules(self):
        @self.pg.production('program : statements')
        def program(p):
            return p[0]

        @self.pg.production('statements : statement')
        @self.pg.production('statements : statements statement')
        def statements(p):
            if len(p) == 1:
                return [p[0]]
            return p[0] + [p[1]]

        @self.pg.production('statement : ID ASSIGN expression')
        def statement_assign(p):
            return Assignment(p[0].getstr(), p[2])

        @self.pg.production('statement : PRINT expression')
        def statement_print(p):
            return Print(p[1])

        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return Number(int(p[0].getstr()))

        @self.pg.production('expression : ID')
        def expression_id(p):
            return Identifier(p[0].getstr())

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_binop(p):
            left = p[0]
            right = p[2]
            operator = p[1].gettokentype()
            return BinaryOp(operator, left, right)

        @self.pg.production('expression : LPAREN expression RPAREN')
        def expression_parens(p):
            return p[1]

        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Ran into a {token.gettokentype()} where it wasn't expected")

    def get_parser(self):
        return self.pg.build() 