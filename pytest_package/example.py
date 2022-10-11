class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


c = Calculator()

# assert condition / assert actual == expected result

assert c.add(1, 2) == 3
assert c.sub(3, 1) == 5




