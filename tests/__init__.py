import os.path
import unittest


def get_tests():
    return full_suite()

def full_suite():
    from .pycat  import PycatTestCase

    pycatsuite = unittest.TestLoader().loadTestsFromTestCase(PycatTestCase)
    return unittest.TestSuite([pycatsuite])
