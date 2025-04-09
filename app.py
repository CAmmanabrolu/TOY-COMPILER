from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from lexer import Lexer
from parser import Parser
from codegen import CodeGenerator
import json
import traceback
import logging
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Store debugger PIN globally
DEBUGGER_PIN = "126-537-827"

def format_ast(ast):
    if isinstance(ast, list):
        return "\n".join(str(node) for node in ast)
    return str(ast)

def analyze_code(source_code):
    try:
        logger.debug(f"Starting code analysis for: {source_code}")
        
        # Create lexer and parser
        lexer = Lexer().get_lexer()
        parser = Parser().get_parser()

        # Tokenize
        logger.debug("Starting tokenization")
        tokens = list(lexer.lex(source_code))
        token_list = [{"type": t.gettokentype(), "value": t.getstr()} for t in tokens]
        logger.debug(f"Generated tokens: {token_list}")

        # Parse
        logger.debug("Starting parsing")
        ast = parser.parse(lexer.lex(source_code))
        logger.debug(f"Generated AST: {ast}")
        
        # Generate code
        logger.debug("Starting code generation")
        codegen = CodeGenerator()
        result = codegen.generate(ast)
        logger.debug(f"Generated code: {result}")

        return {
            "success": True,
            "data": {
                "tokens": token_list,
                "ast": format_ast(ast),
                "result": result,
                "supported_syntax": {
                    "examples": [
                        "x = 5",
                        "print(x)",
                        "2 + 3",
                        "5 * 4",
                        "(2 + 3) * 4"
                    ],
                    "features": [
                        "Variable assignments (x = 5)",
                        "Print statements (print(x))",
                        "Basic arithmetic (+, -, *, /)",
                        "Parentheses for grouping",
                        "Variables must be defined before use"
                    ]
                }
            }
        }
    except Exception as e:
        logger.error(f"Error in analyze_code: {str(e)}")
        logger.error(traceback.format_exc())
        
        error_msg = str(e)
        if "Variable" in error_msg and "is not defined" in error_msg:
            error_msg = f"Error: {error_msg}. Make sure to assign a value to the variable before using it."
        elif "Division by zero" in error_msg:
            error_msg = "Error: Division by zero is not allowed."
        elif "where it wasn't expected" in error_msg:
            error_msg = "Syntax Error: Invalid expression. Please check your syntax."
        
        return {
            "success": False,
            "error": error_msg,
            "debugger_pin": DEBUGGER_PIN,
            "traceback": traceback.format_exc(),
            "supported_syntax": {
                "examples": [
                    "x = 5",
                    "print(x)",
                    "2 + 3",
                    "5 * 4",
                    "(2 + 3) * 4"
                ],
                "features": [
                    "Variable assignments (x = 5)",
                    "Print statements (print(x))",
                    "Basic arithmetic (+, -, *, /)",
                    "Parentheses for grouping",
                    "Variables must be defined before use"
                ]
            }
        }

@app.route('/')
def index():
    logger.debug("Rendering index page")
    return render_template('index.html')

@app.route('/compile', methods=['POST'])
def compile():
    try:
        logger.debug("Received compile request")
        if not request.is_json:
            logger.warning("Request is not JSON")
            return jsonify({"success": False, "error": "Content-Type must be application/json"}), 400

        data = request.get_json()
        if not data or 'code' not in data:
            logger.warning("No code provided in request")
            return jsonify({"success": False, "error": "No code provided"}), 400

        source_code = data['code']
        logger.debug(f"Processing code: {source_code}")
        
        if not isinstance(source_code, str):
            logger.warning("Code is not a string")
            return jsonify({"success": False, "error": "Code must be a string"}), 400

        result = analyze_code(source_code)
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error in compile route: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({
            "success": False, 
            "error": str(e),
            "debugger_pin": DEBUGGER_PIN,
            "traceback": traceback.format_exc()
        }), 500

@app.errorhandler(404)
def not_found_error(error):
    logger.warning("404 error - Page not found")
    return jsonify({"success": False, "error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error("500 error - Internal server error")
    debugger_pin = f"{os.urandom(3).hex()[:6]}"
    return jsonify({
        "success": False, 
        "error": "Internal server error",
        "debugger_pin": debugger_pin
    }), 500

if __name__ == '__main__':
    logger.info("Starting Flask application")
    logger.info(f"Debugger PIN: {DEBUGGER_PIN}")
    app.run(debug=True, host='0.0.0.0', port=5000) 