import pytest
from lib.password_checker import *

def test_check_true():
    password_checker = PasswordChecker()
    assert password_checker.check("12345678") == True

def test_check_exception():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as error:
        password_checker.check("BadPass")
    error_message = str(error.value)
    assert error_message == "Invalid password, must be 8+ characters."