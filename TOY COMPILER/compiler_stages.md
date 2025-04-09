# Toy Compiler Stages

## 1. Lexical Analysis (Lexer) - `lexer.py`
The lexer breaks down the source code into tokens.

Example:
```python
input: x = 5 + 3 * 2
tokens: [
    ID("x"),
    EQUALS,
    NUMBER(5),
    PLUS,
    NUMBER(3),
    MULTIPLY,
    NUMBER(2)
]
```

### Token Types:
- ID: Variable names
- NUMBER: Numeric values
- PLUS, MINUS, MULTIPLY, DIVIDE: Operators
- EQUALS: Assignment operator
- LPAREN, RPAREN: Parentheses
- SEMI: Semicolon
- PRINT: Print keyword

## 2. Syntax Analysis (Parser) - `parser.py`
The parser creates an Abstract Syntax Tree (AST) from tokens.

Example AST for `x = 5 + 3 * 2`:
```
    Assignment
    /        \
   x     BinaryOp(+)
         /          \
        5        BinaryOp(*)
                /          \
               3           2
```

### AST Node Types (`ast_nodes.py`):
- Number: Represents numeric literals
- BinaryOp: Mathematical operations
- Assignment: Variable assignments
- Variable: Variable references
- Print: Print statements

## 3. Code Generation - `codegen.py`
Converts AST into executable code.

Example:
```python
Input AST: Assignment(x, BinaryOp(+, Number(5), BinaryOp(*, Number(3), Number(2))))
Generated: x = 5 + (3 * 2)
```

## Web Interface - `app.py`
The web interface allows you to:
1. Input source code
2. View tokens (Lexer output)
3. View AST (Parser output)
4. See generated code
5. Debug compilation errors

## Example Compilation Flow:

1. Source Code:
```python
x = 5 + 3 * 2
y = x - 4
print(y)
```

2. Lexical Analysis (Tokens):
```python
[ID("x"), EQUALS, NUMBER(5), PLUS, NUMBER(3), MULTIPLY, NUMBER(2), 
 ID("y"), EQUALS, ID("x"), MINUS, NUMBER(4),
 PRINT, LPAREN, ID("y"), RPAREN]
```

3. Syntax Analysis (AST):
```
Program
├── Assignment(x)
│   └── BinaryOp(+)
│       ├── Number(5)
│       └── BinaryOp(*)
│           ├── Number(3)
│           └── Number(2)
├── Assignment(y)
│   └── BinaryOp(-)
│       ├── Variable(x)
│       └── Number(4)
└── Print
    └── Variable(y)
```

4. Code Generation:
```python
x = 5 + (3 * 2)  # x = 11
y = x - 4        # y = 7
print(y)         # Output: 7
```

## Debugging Features:
1. Token visualization
2. AST visualization
3. Step-by-step compilation
4. Error messages for each stage
5. Interactive debugger console

## Common Errors and Debugging:
1. Lexical Errors:
   - Invalid characters
   - Malformed numbers
   - Unknown tokens

2. Syntax Errors:
   - Missing parentheses
   - Invalid expressions
   - Incorrect statement structure

3. Semantic Errors:
   - Undefined variables
   - Type mismatches
   - Invalid operations

## Testing Your Code:
1. Simple Expressions:
```python
x = 5 + 3 * 2
print(x)
```

2. Variables:
```python
x = 10
y = x + 5
print(y)
```

3. Complex Expressions:
```python
x = (5 + 3) * 2
y = x - 4
z = y / 2
print(z)
``` 