# test_runof3.py

from find3 import find3

def test_one(): # test for one run of 3
    num_list = (['one', 'two', 'three', 'four', 'four', 'four', 'five', 'six'])
    assert find3(num_list) == [3]

def test_two(): # check for run of 4 and report 2
    num_list = ([1, 2, 2, 2, 4])

    
    assert find3(num_list) == [1,2]
    
def test_double(): # check for two runs of 3
    num_list = ([48, 47, 47, 47, 19, 23, 14, 14, 14, 18, 48])

    
    assert find3(num_list) == [1,6]

def test_long(): # check for run of 3 with two unique types
    num_list = ([48, 48, 'forty eight', 'forty eight', 'forty eight', 38, 39, -1, 2])

    
    assert find3(num_list) == [2]

def test_none():
    num_list = ([1, 2, 3, 2, 2])
    
    assert find3(num_list) == [0]