import unittest
from HW01 import classify_triangle

class TestTriangle(unittest.TestCase):
    def test1(self):
        self.assertEqual(classify_triangle(3,4,5),'Right Scalene','3,4,5 is a right scalene triangle')
        self.assertEqual(classify_triangle(8,6,10),'Right Scalene','8,6,10 is a right scalene triangle')
    def test2(self):
        self.assertEqual(classify_triangle(2,2,1),'Isoceles','2,2,1 is an isoceles triangle')
        self.assertEqual(classify_triangle(1,2,2),'Isoceles','1,2,2 is an isoceles triangle')
        self.assertEqual(classify_triangle(2,1,2),'Isoceles','2,1,2 is an isoceles triangle')
    def test3(self):
        self.assertEqual(classify_triangle(2,5,6),'Scalene','2,5,6 is a scalene triangle')
    def test4(self):
        self.assertEqual(classify_triangle(9,9,9),'Equilateral','9,9,9 is an equilateral triangle')
    def test5(self):
        self.assertEqual(classify_triangle(3,2,6),'NotATriangle','3,2,6 is not a triangle')

if __name__ == '__main__':
    unittest.main()