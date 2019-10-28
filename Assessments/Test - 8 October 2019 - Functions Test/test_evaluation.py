# test_evaluation.py

from evaluation import *


def test_average_floats():
    assert average_floats(1.0, 2.0, 3.0) == 2.0
    assert average_floats(5432.56, 3454.3322, 7.0) == 2964.6307333333334
    assert average_floats(3.4, 6.1, 3.4) == 4.3


def test_num_woods():
    assert num_woods([1, 1, 2, 5, 7, 9], 2) == 1
    assert num_woods([1, 3, 663, 7653, 146, 1], 9) == 0
    assert num_woods([14, 61, 1, 92132425, 1, 4, 6, 8, 2, 2, 1], 1) == 3


def test_board_list_dict():
    assert board_list_dict([1, 1, 5, 7, 2]) == {1: 2, 2: 1, 5: 1, 7: 1}
    assert board_list_dict([2, 5, 6, 5, 2]) == {2: 2, 5: 2, 6: 1}
    assert board_list_dict([4321, 4321, 23434]) == {23434: 1, 4321: 2}


def test_num_woods_dict():
    assert num_woods_dict({1: 532, 22: 5, 654: 1}, 12) == 0
    assert num_woods_dict({1: 3, 3: 6, 5: 2}, 3) == 6
    assert num_woods_dict({1: 161, 7: 145, 99: 1}, 7) == 145
