class Node:
    def __str__(self):
        return self.__class__.__name__

class Number(Node):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Number({self.value})"

class BinaryOp(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        return f"BinaryOp({self.operator}, {self.left}, {self.right})"

class Assignment(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Assignment({self.name}, {self.value})"

class Print(Node):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Print({self.value})"

class Identifier(Node):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Identifier({self.name})" 