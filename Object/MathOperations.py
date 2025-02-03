class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b
    def calci(self):
        pass


result = MathOperations.add_numbers(5, 3) # 8
print(result)  # 8

math_op = MathOperations()  # creating object of MathOperations class
print(math_op.add_numbers(5, 3))


