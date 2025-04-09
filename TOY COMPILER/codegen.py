class CodeGenerator:
    def __init__(self):
        self.variables = {}
        self.code = []

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_Number(self, node):
        return str(node.value)

    def visit_BinaryOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.operator == 'PLUS':
            return f"({left} + {right})"
        elif node.operator == 'MINUS':
            return f"({left} - {right})"
        elif node.operator == 'MUL':
            return f"({left} * {right})"
        elif node.operator == 'DIV':
            if right == "0":
                raise Exception("Division by zero error!")
            return f"({left} / {right})"

    def visit_Assignment(self, node):
        value = self.visit(node.value)
        self.variables[node.name] = value
        self.code.append(f"{node.name} = {value}")
        return f"{node.name} = {value}"

    def visit_Print(self, node):
        value = self.visit(node.value)
        self.code.append(f"print({value})")
        return f"print({value})"

    def visit_Identifier(self, node):
        if node.name in self.variables:
            return str(self.variables[node.name])
        raise Exception(f"Variable {node.name} is not defined")

    def generate(self, ast):
        for node in ast:
            self.visit(node)
        return '\n'.join(self.code) 