class Computation:
    def __init__(self):
        pass

    def factorial(self, num):
        f = 1
        for i in range(1, num + 1):
            f *= i
        return f

    