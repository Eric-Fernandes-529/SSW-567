# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(2,2,1),'Isoceles','2,2,1 is an isoceles triangle')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2,5,6),'Scalene','2,5,6 is a scalene triangle')

    def testNonTriangles(self):
        self.assertEqual(classifyTriangle(3,2,6),'NotATriangle','3,2,6 is not a triangle')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput','a,b,c is not a valid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

