"""TA lib"""
# pylint: disable=no-member
import numpy
import talib
import unittest

class TestTaLib(unittest.TestCase):
    """Test TA lib"""

    def test_random(self):
        """Test TA lib"""
        numbers = numpy.random.rand(100)
        output = talib.SMA(numbers)
        self.assertIsNotNone(output)

    def test_ta_lib(self):
        """Test TA lib"""
        numbers = numpy.array([1.0, 2.0, 3.0])
        self.assertEqual(1, numpy.min(numbers))
        self.assertEqual(3, numpy.max(numbers))
        output = talib.TSF(numbers, 3)
        self.assertEqual(4, output[-1])
