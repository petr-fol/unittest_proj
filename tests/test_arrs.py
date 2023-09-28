from utils import arrs
import unittest


class test_arrs(unittest.TestCase):
    def test_get(self):
        assert arrs.get([1, 2, 3], 1, "test") == 2
        # было так:  assert arrs.get([1, 2, 3], 1, "test") == 3 ^
        assert arrs.get([], 0, "test") == "test"
        assert arrs.get([1, 2, 3], 6, ) is None

    def test_get_out_of_range_index(self):
        assert arrs.get([1, 2, 3], 10, "test") == "test"
        assert arrs.get([], 0, "test") == "test"

    def test_get_negative_index(self):
        assert arrs.get([1, 2, 3], -1) == 3
        assert arrs.get([1, 2, 3], -2) == 2
        assert arrs.get([1, 2, 3], -4, "test") == "test"

    def test_slice(self):
        assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
        assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]
        assert arrs.my_slice([]) == []


if __name__ == '__main__':
    unittest.main()
# test.discover('tests', pattern='')
