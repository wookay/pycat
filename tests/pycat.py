import sys
import pycat
import unittest

class PycatTestCase(unittest.TestCase):
  def test_int(self):
    self.assertEqual(3, 1+2)
