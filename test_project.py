from project import addition, subtraction, multiplication, division

def main():
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()

def test_addition():
    assert addition(9, 9) == 18
    assert addition(1, 9) == 10
    assert addition(19, 9) == 28

def test_subtraction():
    assert subtraction(9, 9) == 0
    assert subtraction(18, 9) == 9
    assert subtraction(20, 9) == 11

def test_multiplication():
    assert multiplication(9, 9) == 81
    assert multiplication(9, 7) == 63
    assert multiplication(7, 7) == 49

def test_division():
    assert division(9, 9) == 1.0
    assert division(18, 9) == 2.0
    assert division(27, 9) == 3.0

if __name__ == "__main__":
    main()
