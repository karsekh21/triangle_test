import unittest
import triangleCheck

class triangle_test(unittest.TestCase):
    def test_triangle_equilateral (self):
        self.assertEqual(triangleCheck.classify_triangle(7,7,7), "This triangle is equilateral!")

    def test_triangle_isoceles (self):
        self.assertEqual(triangleCheck.classify_triangle(5,5,4), "This triangle is isoceles!")

    def test_triangle_scalene (self):
        self.assertEqual(triangleCheck.classify_triangle(8,5,6), "This triangle is scalene!")

    def test_triangle_right_scalene (self):
        self.assertEqual(triangleCheck.classify_triangle(12,16,20), "This triangle is a right scalene triangle!")

    def test_triangle_right_isoceles (self):
        self.assertEqual(triangleCheck.classify_triangle(4,4,5.7), "This triangle is a right isoceles!")

if __name__ == '__main__':
    unittest.main()
