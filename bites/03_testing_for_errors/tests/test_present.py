import pytest
from lib.present import *

def test_init():
    present = Present()
    assert present.contents == None

def test_first_wrap():
    present = Present()
    present.wrap("contents")
    assert present.contents == "contents"

def test_second_wrap():
    present = Present()
    present.wrap("contents")
    with pytest.raises(Exception) as error:
        present.wrap("other contents")
    error_message = str(error.value)
    assert error_message == "A contents has already been wrapped."

def test_first_unwrap():
    present = Present()
    with pytest.raises(Exception) as error:
        present.unwrap()
    error_message = str(error.value)
    assert error_message == "No contents have been wrapped."

def test_second_unwrap():
    present = Present()
    present.wrap("contents")
    present.unwrap()
    assert present.contents == "contents"