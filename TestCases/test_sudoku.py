# test_sudoku.py
#
# http://opencvpython.blogspot.kr/2012/06/sudoku-solver-part-1.html

import cv2
import numpy as np

def test_sudoku_square():
  img = cv2.imread('res/sudoku.jpg')
  rows,cols,ch = img.shape
  dst = np.array([
    [  0.,   0.],
    [449.,   0.],
    [449., 449.],
    [  0., 449.]], np.float32)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  #cv2.imshow('', gray)
  #cv2.waitKey()
  thresh = cv2.adaptiveThreshold(gray,255,1,1,5,2)
  #cv2.imshow('', thresh)
  #cv2.waitKey()
  _,contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  image_area = gray.size
  approx = None
  for i in contours:
    if cv2.contourArea(i)> image_area/2:
      peri = cv2.arcLength(i,True)
      approx = cv2.approxPolyDP(i, 0.1*peri, True)
      Blue = (255,0,0)
      cv2.drawContours(img, [approx], 0, Blue, 2,0)
      #cv2.imshow('', img)
      #cv2.waitKey()
  assert_equal([
    [[491,  68]],
    [[ 73,  84]],
    [[ 34, 516]],
    [[520, 522]]], approx)
  #cv2.imshow('', img)
  #cv2.waitKey()
  #Red = (0,0,255)
  #cv2.polylines(img, [approx], True, Red, 2)
  #cv2.imshow('', img)
  #cv2.waitKey()



# What are contours?
#   Contours can be explained simply as a curve joining all the continuous
#   points (along the boundary), having same color or intensity. The contours
#   are a useful tool for shape analysis and object detection and recognition.

# cv2.arcLength
#   Calculates a contour perimeter or a curve length.
#   The function computes a curve length or a closed contour perimeter.

# cv2.approxPolyDP
#   Approximates a polygonal curve(s) with the specified precision.
#   The functions approxPolyDP approximate a curve or a polygon with another
#   curve/polygon with less vertices so that the distance between them is
#   less or equal to the specified precision.
#   It uses the Douglas-Peucker algorithm


def test_perspective_transform():
  img = cv2.imread('res/sudoku.jpg')
  rows,cols,ch = img.shape
  src = np.array([
    [[491,  68]],
    [[ 73,  84]],
    [[ 34, 516]],
    [[520, 522]]], np.float32)
  src = rect_clockwise(src)
  assert_equal([
    [ 73,  84],
    [491,  68],
    [520, 522],
    [ 34, 516]], src)
  dst = np.array([
    [  0.,   0.],
    [449.,   0.],
    [449., 449.],
    [  0., 449.]], np.float32)
  t = cv2.getPerspectiveTransform(src,dst)
  imgdst = cv2.warpPerspective(img,t,(450,450))
  assert_true(imgdst.dtype == np.uint8)
  assert_equal([450, 450, 3], imgdst.shape)
  #cv2.imshow('', imgdst)
  #cv2.waitKey()

def rect_clockwise(h):
  h = h.reshape((4,2))
  hnew = np.zeros((4,2),dtype = np.float32)
  add = h.sum(1)
  hnew[0] = h[np.argmin(add)]
  hnew[2] = h[np.argmax(add)]
  diff = np.diff(h,axis = 1)
  hnew[1] = h[np.argmin(diff)]
  hnew[3] = h[np.argmax(diff)]
  return hnew

  

from numpy.testing import assert_, assert_array_equal, assert_allclose, run_module_suite
def assert_true(a):
  assert_(a)
def assert_equal(a,b):
  if type(a) or type(b) is np.ndarray:
    if type(a) is np.ndarray and a.dtype == np.float64:
      assert_allclose(a, b)
    elif type(b) is np.ndarray and b.dtype == np.float64:
      assert_allclose(a, b)
    else:
      assert_array_equal(a, b)
  else:
    assert_(a==b)

if __name__=="__main__":
  run_module_suite()
