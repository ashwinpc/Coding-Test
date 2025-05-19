class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"

# User input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

calc = Calculator(a, b, operation)
print("Result:", calc.calculate())
