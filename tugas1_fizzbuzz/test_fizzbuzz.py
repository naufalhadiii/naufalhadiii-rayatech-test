from fizzbuzz import fizzbuzz

def test_angka_biasa():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(7) == "7"

def test_kelipatan_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(99) == "Fizz"

def test_kelipatan_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(100) == "Buzz"

def test_kelipatan_3_dan_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"