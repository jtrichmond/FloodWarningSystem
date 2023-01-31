"""Unit test for the utils module"""

from audioop import reverse
import floodsystem.utils


def test_sort():
    """Test sort container by specific index"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2)
    assert list1[0] == b
    assert list1[1] == a
    assert list1[2] == c


def test_reverse_sort():
    """Test sort container by specific index (reverse)"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2, reverse=True)
    assert list1[0] == c
    assert list1[1] == a
    assert list1[2] == b


def test_sort_by_property():
    """Test sort on container based on its properties"""
    class TestObject:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    first = TestObject(0,5,18)
    second = TestObject(8,1,20)
    third = TestObject(4,5,6)
    test_list = [first, second, third]

    test_list = floodsystem.utils.sorted_by_property(test_list, "x")
    assert test_list == [first, third, second]

    test_list = floodsystem.utils.sorted_by_property(test_list, "y")
    assert test_list[0] == second
    assert test_list[1] in {first, third}
    assert test_list[2] in {first, third} 

    test_list = floodsystem.utils.sorted_by_property(test_list, "z", reverse=True)
    assert test_list == [second, first, third]



