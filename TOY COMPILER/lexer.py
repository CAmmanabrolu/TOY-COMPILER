from rply import LexerGenerator

class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()
        self._add_tokens()

    def _add_tokens(self):
        # Keywords
        self.lexer.add('PRINT', r'print')
        self.lexer.add('ASSIGN', r'=')

        # Operators
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')
        self.lexer.add('LPAREN', r'\(')
        self.lexer.add('RPAREN', r'\)')

        # Numbers and identifiers
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('ID', r'[a-zA-Z_][a-zA-Z0-9_]*')

        # Ignore whitespace
        self.lexer.ignore('\s+')

    def get_lexer(self):
        return self.lexer.build() 