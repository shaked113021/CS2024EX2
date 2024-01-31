import unittest
from unittest.mock import patch
import io
import question3


class UpperTriangleTests(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_CheckWithSquareMatrix(self, fake_out: io.StringIO):
        mat_input = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        expected_output = ("1    2    3    \n"
                           "     5    6    \n"
                           "          9    \n")

        question3.print_upper_triangle(mat_input)
        self.assertEqual(expected_output, fake_out.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_CheckWithMoreColsThanRows(self, fake_out: io.StringIO):
        mat_input = [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18]
        ]

        self.assertRaises(ValueError, question3.print_upper_triangle, mat_input)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_CheckNotMatrix(self, fake_out=io.StringIO):
        self.assertRaises(TypeError, question3.print_upper_triangle, 5)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_checkInnerNotMatrix(self, fake_out: io.StringIO):
        mat_input = [
            [1, 2, 3, 4, 5],
            6,
            [7, 8, 9, 10, 11]
        ]
        self.assertRaises(ValueError, question3.print_upper_triangle, mat_input)


if __name__ == '__main__':
    unittest.main()
