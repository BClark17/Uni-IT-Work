"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_07.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    repeated_string = [s]*n
    return " ".join(repeated_string)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def phrase_to_sentence(phrase):
    """
    Turn a phrase into a sentence
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('it is an ex parrot')
    'It is an ex parrot.'
    >>> phrase_to_sentence('exams are in two weeks')
    'Exams are in two weeks.'
    """
    sentence = phrase.split(" ")
    if sentence[-1].endswith("."):
        return " ".join(sentence).capitalize()
    else:
        return " ".join(sentence).capitalize() + "."


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0, "Car does not set default fuel input properly"

    test_car = Car(10)
    assert test_car.fuel == 10, "Car does not set fuel input properly"




run_tests()

doctest.testmod()
