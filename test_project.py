import pytest
from word2number import w2n
from project import parse_input, combine_number_words, convert, evaluate

def test_parse_input():
    assert parse_input("what is twenty plus five") == ["twenty", "plus", "five"]
    assert parse_input("how about one hundred divided by ten") == ["one hundred", "divided", "ten"]
    assert parse_input("just two") == ["two"]

def test_combine_number_words():
    assert combine_number_words(["twenty", "five", "plus", "two"]) == ["twenty five", "plus", "two"]
    assert combine_number_words(["one", "hundred", "divided", "ten"]) == ["one hundred", "divided", "ten"]
    assert combine_number_words(["minus", "five"]) == ["minus", "five"]

def test_convert():
    assert convert(["twenty five", "plus", "two"]) == [25, "plus", 2]
    assert convert(["one hundred", "divided", "ten"]) == [100, "divided", 10]
    assert convert(["minus", "five"]) == ["minus", 5]

def test_evaluate_add_sub():
    assert evaluate([25, "plus", 2]) == 27
    assert evaluate([10, "minus", 3]) == 7
    assert evaluate([50, "add", 10]) == 60
    assert evaluate([100, "subtract", 50]) == 50

def test_evaluate_mul_div():
    assert evaluate([5, "times", 6]) == 30
    assert evaluate([20, "divided", 5]) == 4
    assert evaluate([10, "over", 2]) == 5

def test_order_of_operations():
    # Should evaluate 10 / 2 first, then add 3 => 5 + 3 = 8
    assert evaluate([10, "divided", 2, "plus", 3]) == 8
    # Should evaluate 4 * 5 = 20, then 2 + 20 = 22
    assert evaluate([2, "plus", 4, "times", 5]) == 22


