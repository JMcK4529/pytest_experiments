from lib.gratitudes import *

def test_init():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

def test_add():
    gratitudes = Gratitudes()
    results = []
    for word in ["apples", "bananas", "cherries"]:
        gratitudes.add(word)
        print(results)
        results.append(gratitudes.gratitudes.copy())
        print(f"{word} : {results}")
    assert results == [["apples"], ["apples", "bananas"], ["apples", "bananas", "cherries"]]

def test_format():
    gratitudes = Gratitudes()
    for word in ["apples", "bananas", "cherries"]:
        gratitudes.add(word)
    results = gratitudes.format()
    assert results == "Be grateful for: apples, bananas, cherries"