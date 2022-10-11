class CheckEvenOdd:

    def even(self, num):
        return num % 2

    def odd(self, num):
        return num % 2 == 1


eo = CheckEvenOdd()


def test_even():
    print("In test even method")
    assert eo.even(5) == 0, "Number is odd"


def test_odd():
    print("in test odd method")
    assert eo.odd(10), "Number is even"

