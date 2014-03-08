# test_numpy.py

# http://wiki.scipy.org/Tentative_NumPy_Tutorial

from numpy import arange, dtype, ndarray, array
def test_basic():
  a = arange(15).reshape(3, 5)
  assert_equal([[0,  1,  2,  3,  4],
                [5,  6,  7,  8,  9],
                [10, 11, 12, 13, 14]], a)
  assert_equal((3, 5), a.shape)
  assert_equal(2, a.ndim)
  assert_equal(dtype('int64'), a.dtype)
  assert_equal(8, a.itemsize)
  assert_equal(15, a.size)
  assert_true(type(a) is ndarray)
  b = array([6, 7, 8])
  assert_true(type(b) is ndarray)
  
from numpy import ones, zeros, linspace
def test_array_creation():
  a = array([2,3,4])
  assert_equal(dtype('int64'), a.dtype)
  b = array([1.2, 3.5, 5.1])
  assert_equal(dtype('float64'), b.dtype)
  assert_equal([1., 1., 1.], ones(3))
  assert_equal([[0., 0., 0., 0.],
                [0., 0., 0., 0.],
                [0., 0., 0., 0.]], zeros((3,4)))
  c = arange(10, 30, 5)
  assert_equal([10, 15, 20, 25], c)
  d = arange(0, 2, 0.3)
  assert_equal([0., 0.3, 0.6, 0.9, 1.2, 1.5, 1.8], d)
  e = linspace(0, 2, 9)
  assert_equal([0., 0.25, 0.5, 0.75, 1., 1.25, 1.5, 1.75, 2.], e)

from numpy import sin
def test_basic_operations():
  a = array([20,30,40,50])
  b = arange(4)
  assert_equal([0, 1, 2, 3], b)
  assert_equal([20, 29, 38, 47], a-b)
  assert_equal([0, 1, 4, 9], b**2)
  assert_equal([9.12945251, -9.88031624,  7.4511316 , -2.62374854], 10*sin(a))
  assert_equal([True, True, False, False], a<35)
  assert_equal(6, b.sum())

from numpy.linalg import solve
def test_linear_algebra():
  # 3x + 1y = 9
  # 1x + 2y = 8
  a = array([[3,1], [1,2]])
  b = array([9,8])
  x = solve(a,b)
  assert_equal([2., 3.], x)
 


from numpy.testing import assert_, assert_array_equal, assert_allclose, run_module_suite
def assert_true(a):
  assert_(a)
def assert_equal(a,b):
  if type(a) or type(b) is ndarray:
    if type(a) is ndarray and a.dtype == dtype('float64'):
      assert_allclose(a, b)
    elif type(b) is ndarray and b.dtype == dtype('float64'):
      assert_allclose(a, b)
    else:
      assert_array_equal(a, b)
  else:
    assert_(a==b)

if __name__=="__main__":
  run_module_suite()
