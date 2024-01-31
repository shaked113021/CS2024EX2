import unittest
from unittest import TestCase
import question8


class EfficientMergeTests(TestCase):

    def test_CheckTwoListsInOrder(self):
        list_a = [1, 2, 3, 4, 5]
        list_b = [6, 7, 8, 9, 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        result = question8.merge_efficient(list_a, list_b)
        self.assertListEqual(expected, result)

    def test_CheckTwoListNotInOrder(self):
        list_a = [1, 3, 5, 7, 9]
        list_b = [2, 4, 6, 8, 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        result = question8.merge_efficient(list_a, list_b)
        self.assertListEqual(expected, result)

    def test_CheckTwoListNotInOrderReversed(self):
        list_a = [2, 4, 6, 8, 10]
        list_b = [1, 3, 5, 7, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        result = question8.merge_efficient(list_a, list_b)
        self.assertListEqual(expected, result)

    def test_CheckTwoListsRepeatingValue(self):
        list_a = [2, 4, 6, 8, 10]
        list_b = [1, 4, 5, 7, 9]
        expected = [1, 2, 4, 4, 5, 6, 7, 8, 9, 10]

        result = question8.merge_efficient(list_a, list_b)
        self.assertListEqual(expected, result)

    def test_CheckFirstArgIsNotList(self):
        list_b = [1, 4, 8, 17]
        self.assertRaises(TypeError, question8.merge_efficient, 9, list_b)

    def test_CheckSecondArgIsNotList(self):
        list_a = [1, 9 ,10 ,12]
        self.assertRaises(TypeError, question8.merge_efficient, list_a, 9)


if __name__ == '__main__':
    unittest.main()
