class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if (b<0):
            a = self.subtract(0,a)
            b = self.subtract(0,b)
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if (b==0):
            raise ZeroDivisionError("Cannot divide by zero")
        result = 0
        check = False
        if a < 0:
            a = self.subtract(0, a)
            check = not check
        if (b<0):
            b = self.subtract(0,b)
            check = not check
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if (check):
            return self.subtract(0,result)
        else:
            return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero")
        
        check_a = False
        check_b = False
        if a < 0:
            a = self.subtract(0, a)
            check_a = not check_a
        if b < 0:
            b = self.subtract(0, b)
            check_b = not check_b
        
        while a >= b:
            a = a-b
        if a == 0:
            return 0
        if check_a and check_b:
            return self.subtract(0, a)
        elif check_a:
            return self.subtract(b, a)
        elif check_b:
            return self.subtract(a, b)
        else:
            return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))