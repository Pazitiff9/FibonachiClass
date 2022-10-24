class Fibonachi:

    def __init__(self, n):
        self.number = n
        self.value = self.__calc_fib()

    def __add__(self, other):
        self.number += other
        self.value = self.__calc_fib()
        return self

    def __sub__(self, other):
        self.number -= other
        self.value = self.__calc_fib()
        return self

    def __calc_fib(self, a=0, b=1):
        for _ in range(self.number):
            a, b = b, a + b
        return a
