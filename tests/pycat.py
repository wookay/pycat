import unittest
from pkg_resources import parse_version
import pycat
import types

class PycatTestCase(unittest.TestCase):

  def test_pycat(self):
    a = pycat.Pycat()
    self.assertEqual(type(a), pycat.Pycat)
    self.assertTrue(parse_version(pycat.__version__) >= parse_version('0.0.2'))

  def test_int(self):
    self.assertEqual(3, 1+2)

  def test_type(self):
    def f():
      pass
    self.assertTrue(isinstance(f, types.FunctionType))
