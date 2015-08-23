import sys
import pycat

import sys
if sys.version_info[:2] == (2, 6):
    try:
        import unittest2 as unittest
    except ImportError:
        raise Exception('The test suite requires unittest2 on Python 2.6')
else:
    import unittest
#import unittest2 as unittest

class PycatTestCase(unittest.TestCase):
  def test_int(self):
    self.assertEqual(3, 1+2)
