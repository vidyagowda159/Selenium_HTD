class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


c = Calculator()


def test_add():
    assert c.add(1, 10) == 3, "The sum is not 3"


def test_sub():
    assert c.sub(3, 1) == 5, "The difference is not 5"
