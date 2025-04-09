from flask import Flask, render_template, request, jsonify
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
                "result": result
            }
        }
    except Exception as e:
        logger.error(f"Error in analyze_code: {str(e)}")
        logger.error(traceback.format_exc())
        
        # Only generate debugger PIN for actual errors
        error_msg = str(e)
        debugger_pin = None
        
        # Check if it's an actual error that needs debugging
        if "SourcePosition" in error_msg or "Division by zero" in error_msg or "NameError" in error_msg or "SyntaxError" in error_msg:
            debugger_pin = f"{os.urandom(3).hex()[:6]}"
            
            # Provide more descriptive error messages
            if "SourcePosition" in error_msg:
                error_msg = "Syntax error: Invalid expression. Please check for:\n" + \
                           "1. Missing operators between expressions\n" + \
                           "2. Invalid operator combinations\n" + \
                           "3. Unmatched parentheses\n" + \
                           "4. Missing semicolons between statements"
            elif "Division by zero" in error_msg:
                error_msg = "Runtime error: Division by zero is not allowed"
            elif "NameError" in error_msg:
                error_msg = "Error: Variable not defined. Make sure to assign a value before using it"
            elif "SyntaxError" in error_msg:
                error_msg = "Syntax error: " + error_msg.split("SyntaxError: ")[-1]
        
        return {
            "success": False,
            "error": error_msg,
            "debugger_pin": debugger_pin
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
        if not result.get("success", True):
            return jsonify(result), 500
        return jsonify({"success": True, "data": result})
    except Exception as e:
        logger.error(f"Error in compile route: {str(e)}")
        logger.error(traceback.format_exc())
        # Generate a random PIN for debugging
        debugger_pin = f"{os.urandom(3).hex()[:6]}"
        return jsonify({
            "success": False, 
            "error": str(e),
            "debugger_pin": debugger_pin
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
    app.run(debug=True) 