from lib.counter import *

def test_init():
    counter = Counter()
    assert counter.count == 0
def test_add():
    counter = Counter()
    results = []
    for i in range(1,6):
        counter.add(i)
        results.append(counter.count)
    assert results == [1,3,6,10,15]
def test_report():
    counter = Counter()
    results = []
    results.append(counter.report())
    counter.add(5)
    results.append(counter.report())
    assert results == ["Counted to 0 so far.", "Counted to 5 so far."]
