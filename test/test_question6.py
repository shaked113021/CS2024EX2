import unittest
from unittest import TestCase
import question6


class SelectionSortTests(TestCase):

    def test_CheckSortedArray(self):
        to_sort = [1, 3, 6, 7]
        expected = [1, 3, 6, 7]
        question6.selection_sort(to_sort)
        self.assertListEqual(expected, to_sort)

    def test_CheckUnsortedArray(self):
        to_sort = [2, 1, 5, 9, 8]
        expected = [1, 2, 5, 8, 9]
        question6.selection_sort(to_sort)
        self.assertListEqual(expected, to_sort)

    def test_CheckSortedStrings(self):
        to_sort = ['a', 'b', 'c', 'd']
        expected = ['a', 'b', 'c', 'd']
        question6.selection_sort(to_sort)
        self.assertListEqual(expected, to_sort)

    def test_CheckUnsortedStrings(self):
        to_sort = ['d', 'b', 'c', 'a', 'f']
        expected = ['a', 'b', 'c', 'd', 'f']
        question6.selection_sort(to_sort)
        self.assertListEqual(expected, to_sort)

    def test_NotList(self):
        self.assertRaises(TypeError, question6.selection_sort, 8)


if __name__ == '__main__':
    unittest.main()
