import unittest
from unittest import TestCase
import question5


class IsPalindromeTests(TestCase):

    def test_oddStringPalindrome(self):
        self.assertTrue(question5.is_palindrome('aba'))

    def test_oddStringNotPalindrome(self):
        self.assertFalse(question5.is_palindrome('abc'))

    def test_evenStringPalindrome(self):
        self.assertTrue(question5.is_palindrome('abba'))

    def test_evenStringNotPalindrome(self):
        self.assertFalse(question5.is_palindrome('abca'))


if __name__ == '__main__':
    unittest.main()
