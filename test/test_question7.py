from unittest import TestCase
import unittest
import question7


class NonEfficientMergeTests(TestCase):

    def test_CheckTwoListsInOrder(self):
        list_a = [1, 2, 3, 4, 5, 6]
        list_b = [7, 8, 9, 10, 11, 12]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        result = question7.merge_lists_not_efficient(list_a, list_b)
        self.assertListEqual(expected, result)

    def test_CheckTwoListsNotInOrderValues(self):
        list_a = [1, 3, 5, 7, 9, 11]
        list_b = [2, 4, 6, 8, 10, 12]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        result = question7.merge_lists_not_efficient(list_a, list_b)
        self.assertListEqual(expected, result)

    def test_FirstArgIsNotList(self):
        list_b = [2, 4, 6, 8]
        self.assertRaises(TypeError, question7.merge_lists_not_efficient, 8, list_b)

    def test_SecondArgIsNotList(self):
        list_a = [1, 2, 3, 4]
        self.assertRaises(TypeError, question7.merge_lists_not_efficient, list_a, 9)


if __name__ == '__main__':
    unittest.main()