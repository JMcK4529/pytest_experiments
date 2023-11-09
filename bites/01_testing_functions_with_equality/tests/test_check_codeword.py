from lib.check_codeword import *

def test_check_codeword_correct():
    assert check_codeword("horse") == "Correct! Come in."
def test_check_codeword_close():
    assert check_codeword("heave") == "Close, but nope."
def test_check_codeword_wrong():
    assert check_codeword("sheep") == "WRONG!"