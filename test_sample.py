# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
def test_float():
    assert inc(2.1) == 3.0

