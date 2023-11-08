from lib.report_length import *

def test_report_length_four():
    assert report_length("four") == "This string was 4 characters long."
def test_report_length_long():
    assert report_length("012345678911234567892123456789") == "This string was 30 characters long."
def test_report_length_empty():
    assert report_length("") == "This string was 0 characters long."