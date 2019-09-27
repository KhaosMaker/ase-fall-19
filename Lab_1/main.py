import calculator as c


class FooCalculator:

    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m, n)

    def substract(self, m, n):
        return c.subtract(m, n)

    def divide(self, m, n):
        return c.divide(m, n)

    def multiply(self, m, n):
        return c.multiply(m, n)


calc = FooCalculator()

m = int(input("Insert a value for m: "))
n = int(input("Insert a value for n: "))

print(m, "+", n, "=", calc.sum(m, n))
assert m+n == calc.sum(m, n)

try:
    print(m, "/", n, "=", calc.divide(m, n))
    assert int(m/n) == calc.divide(m, n)
except AssertionError:
    print("You can't divide by 0, idiot!")

print(m, "*", n, "=", calc.multiply(m, n))
assert m*n == calc.multiply(m, n)
