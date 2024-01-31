import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import question4


class StarPatternTests(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_CheckGivenExampleMatchesRequirement(self, fake_out: StringIO):
        expected_pattern = '********@******@****@**@\n'

        question4.print_star_pattern(8)
        self.assertEqual(expected_pattern, fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
