import unittest
import question2


class XORTests(unittest.TestCase):

    def test_CheckBothZeroExpectsZero(self):
        self.assertEqual(0, question2.xor_gate(0, 0))

    def test_CheckZeroAndOneExpectsOne(self):
        self.assertEqual(1, question2.xor_gate(0, 1))

    def test_CheckOneAndZeroExpectsOne(self):
        self.assertEqual(1, question2.xor_gate(1, 0))

    def test_CheckBothOneExpectsZero(self):
        self.assertEqual(0, question2.xor_gate(1, 1))

    def test_CheckTwoAndZeroExpectsValueError(self):
        self.assertRaises(ValueError, question2.xor_gate, 2, 0)

    def test_CheckZeroAndFiveExpectsValueError(self):
        self.assertRaises(ValueError, question2.xor_gate, 0, 5)

    def test_CheckZeroAndAFloatExpectsTypeError(self):
        self.assertRaises(TypeError, question2.xor_gate, 0, 2.4)

    def test_CheckFloatAndZeroExpectsTypeError(self):
        self.assertRaises(TypeError, question2.xor_gate, 2.4, 0)


class NANDTests(unittest.TestCase):

    def test_CheckBothZeroExpectsOne(self):
        self.assertEqual(1, question2.nand_gate(0, 0))

    def test_CheckZeroAndOneExpectsOne(self):
        self.assertEqual(1, question2.nand_gate(0, 1))

    def test_CheckOneZeroExpectsOne(self):
        self.assertEqual(1, question2.nand_gate(1, 0))

    def test_CheckBothOneExpectsZero(self):
        self.assertEqual(0, question2.nand_gate(1, 1))

    def test_CheckThreeAndZeroExpectsValueError(self):
        self.assertRaises(ValueError, question2.nand_gate, 3, 0)

    def test_CheckZeroAndThreeExpectsValueError(self):
        self.assertRaises(ValueError, question2.nand_gate, 0, 3)

    def test_CheckZeroAndFloatExpectsTypeError(self):
        self.assertRaises(TypeError, question2.nand_gate, 0, 2.4)

    def test_CheckFloatAndZeroExpectsTypeError(self):
        self.assertRaises(TypeError, question2.nand_gate, 2.4, 0)


class ANDTests(unittest.TestCase):

    def test_CheckBothZeroExpectsZero(self):
        self.assertEqual(0, question2.and_gate(0, 0))

    def test_CheckZeroAndOneExpectsZero(self):
        self.assertEqual(0, question2.and_gate(0, 1))

    def test_CheckOneAndZeroExpectsZero(self):
        self.assertEqual(0, question2.and_gate(1, 0))

    def test_CheckBothOneExpectsOne(self):
        self.assertEqual(1, question2.and_gate(1, 1))

    def test_CheckTwoAndZeroExpectsValueError(self):
        self.assertRaises(ValueError, question2.and_gate, 2, 0)

    def test_CheckZeroAndFiveExpectsValueError(self):
        self.assertRaises(ValueError, question2.and_gate, 0, 5)

    def test_CheckZeroAndAFloatExpectsTypeError(self):
        self.assertRaises(TypeError, question2.and_gate, 0, 2.4)

    def test_CheckFloatAndZeroExpectsTypeError(self):
        self.assertRaises(TypeError, question2.and_gate, 2.4, 0)


class ORTests(unittest.TestCase):

    def test_CheckBothZeroExpectsZero(self):
        self.assertEqual(0, question2.or_gate(0, 0))

    def test_CheckOneAndZeroExpectsOne(self):
        self.assertEqual(1, question2.or_gate(1, 0))

    def test_CheckZeroAndOneExpectsOne(self):
        self.assertEqual(1, question2.or_gate(0, 1))

    def test_CheckBothOneExpectsOne(self):
        self.assertEqual(1, question2.or_gate(1, 1))

    def test_CheckTwoAndZeroExpectsValueError(self):
        self.assertRaises(ValueError, question2.or_gate, 2, 0)

    def test_CheckZeroAndFiveExpectsValueError(self):
        self.assertRaises(ValueError, question2.or_gate, 0, 5)

    def test_CheckZeroAndAFloatExpectsTypeError(self):
        self.assertRaises(TypeError, question2.or_gate, 0, 2.4)

    def test_CheckFloatAndZeroExpectsTypeError(self):
        self.assertRaises(TypeError, question2.or_gate, 2.4, 0)


if __name__ == '__main__':
    unittest.main()
