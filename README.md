# Toy Compiler

A simple, interactive toy compiler that demonstrates basic compiler concepts including lexical analysis, parsing, and code generation. This project provides a web interface for experimenting with a subset of Python-like syntax.

## Features

- **Interactive Web Interface**: Compile and run code directly in your browser
- **Lexical Analysis**: Tokenize input code into meaningful symbols
- **Parsing**: Generate Abstract Syntax Trees (AST) from tokens
- **Code Generation**: Execute simple arithmetic and variable operations
- **Debug Support**: Built-in debugger with error tracking
- **Real-time Feedback**: See tokens, AST, and execution results instantly

## Supported Syntax

The compiler supports a subset of Python-like syntax:

```python
# Variable assignments
x = 5

# Print statements
print(x)

# Basic arithmetic
2 + 3
5 * 4
(2 + 3) * 4

# Multiple operations
a = 10
b = 5
print(a + b)
```

## Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)



### Successful Compilation
![Successful Compilation](screenshots/successful_compilation.png)

### Error Handling
![image](https://github.com/user-attachments/assets/3ac2bbb5-94c5-4d4a-80c1-b84091d7787d)


## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/toy-compiler.git
cd toy-compiler
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

## Project Structure

```
toy-compiler/
├── app.py              # Main Flask application
├── lexer.py           # Lexical analyzer
├── parser.py          # Parser implementation
├── codegen.py         # Code generator
├── ast_nodes.py       # Abstract Syntax Tree nodes
├── requirements.txt   # Project dependencies
├── templates/         # HTML templates
│   └── index.html    # Main web interface
└── README.md         # Project documentation
```

## Debugging

The application includes a built-in debugger. When you encounter an error:
1. The debugger PIN will be displayed in the terminal
2. Error details and traceback will be shown in the web interface
3. Use the debugger PIN to access detailed debugging information

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
