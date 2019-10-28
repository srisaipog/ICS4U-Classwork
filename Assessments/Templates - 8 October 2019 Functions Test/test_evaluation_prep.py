import evaluation_prep

def test_add():
    assert evaluation_prep.add(1, 1) == 2
    assert evaluation_prep.add(114, 111) == 225
    assert evaluation_prep.add(1, 131) == 132


def test_add_list():
    assert evaluation_prep.add_list([1, 2, 3]) == 6
    assert evaluation_prep.add_list([1, 2, 9]) == 12
    assert evaluation_prep.add_list([1, 2, 12]) == 15


def test_num_times():

    words = ["bob", "bill", "bob"]
    times = {"bob": 2, "bill": 1}
    assert evaluation_prep.num_times(words) == times

    words = ["bill", "bob", "bill", "bob", "bob"]
    times = {"bob": 3, "bill": 2}
    assert evaluation_prep.num_times(words) == times

    words = ["blip", "blop", "blip", "blip"]
    times = {"blip": 3, "blop": 1}
    assert evaluation_prep.num_times(words) == times

