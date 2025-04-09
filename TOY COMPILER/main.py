import sys
from lexer import Lexer
from parser import Parser
from codegen import CodeGenerator

def compile_code(source_code):
    # Create lexer and parser
    lexer = Lexer().get_lexer()
    parser = Parser().get_parser()

    # Tokenize and parse
    tokens = lexer.lex(source_code)
    ast = parser.parse(tokens)

    # Generate code
    codegen = CodeGenerator()
    result = codegen.generate(ast)

    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            source_code = file.read()
        
        result = compile_code(source_code)
        print(result)
        
    except FileNotFoundError:
        print(f"Error: File {sys.argv[1]} not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 