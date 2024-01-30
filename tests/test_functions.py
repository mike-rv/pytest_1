from lib.functions import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8


def test_check_codeword():

    assert check_codeword("horse") == "Correct! Come in."
    assert check_codeword("hootee") == "Close, but nope."
    assert check_codeword("Garble garble") == "WRONG!"


def test_greet_returns_hello_name():
    result = greet("Bob")
    assert result == "Hello, Bob!"


def test_report_length():

    assert report_length("one two ten") == "This string was 11 characters long."

    assert report_length("humpty dumpty sat on a wall") == "This string was 27 characters long."

    assert report_length("mmmmmmmm gravy") == "This string was 14 characters long."