# Toy Compiler

This is a simple toy compiler that can handle basic arithmetic expressions. It demonstrates the fundamental concepts of compiler design including lexical analysis, parsing, and code generation.

## Features
- Lexical analysis (tokenization)
- Parsing of arithmetic expressions
- Simple code generation
- Support for basic arithmetic operations (+, -, *, /)
- Support for numbers and variables

## Project Structure
- `lexer.py`: Handles tokenization of input
- `parser.py`: Parses tokens into an AST (Abstract Syntax Tree)
- `codegen.py`: Generates code from the AST
- `main.py`: Main entry point of the compiler
- `requirements.txt`: Project dependencies

## Usage
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the compiler:
```bash
python main.py input_file.txt
```

## Example Input
```
x = 5 + 3 * 2
y = x - 4
print(y)
```

## Example Output
```
x = 11
y = 7
``` 