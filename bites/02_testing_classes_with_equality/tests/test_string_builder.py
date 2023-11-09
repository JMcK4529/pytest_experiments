from lib.string_builder import *

def test_init():
    string_builder = StringBuilder()
    assert string_builder.str == ""
def test_add():
    string_builder = StringBuilder()
    results = []
    for character in "foobar":
        string_builder.add(character)
        results.append(string_builder.str)
    assert results == ["f", "fo", "foo", "foob", "fooba", "foobar"]
def test_size():
    string_builder = StringBuilder()
    results = []
    for character in "foobar":
        string_builder.add(character)
        results.append(string_builder.size())
    assert results == [1,2,3,4,5,6]
def test_output():
    string_builder = StringBuilder()
    results = []
    for character in "foobar":
        string_builder.add(character)
        results.append(string_builder.str == string_builder.output())
    assert all(results)