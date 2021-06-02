import pytest
import reverser

def test_reverser1():
    result = reverser.reverse("This is a test")
    assert result == "test a is This"

def test_reverser2():
    result = reverser.reverse("Software Engineering 2")
    assert result == "2 Engineering Software"

def test_reverser3():
    result = reverser.reverse("Hello. My name is Adam.")
    assert result == "Adam is name My Hello.."