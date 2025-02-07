class MathUtils:
    @staticmethod
    def add(a, b):
        """Returning sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Return the result of subtracting b from a"""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Return the product of two numbers"""
        return a * b

    @staticmethod
    def divide(a, b):
        """Return result of diving a by b"""
        if b == 0:
            return -1.0
        return a / b

print(MathUtils.multiply(6, 9 ))
print(MathUtils.divide(3, 9 ))