from lib.report_length import *

def test_report_length():

    assert report_length("one two ten") == "This string was 11 characters long."

    assert report_length("humpty dumpty sat on a wall") == "This string was 27 characters long."

    assert report_length("mmmmmmmm gravy") == "This string was 14 characters long."