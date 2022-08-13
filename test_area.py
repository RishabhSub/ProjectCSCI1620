from area_formulas import *
import unittest
from math import pi


class TestArea(unittest.TestCase):
    def test_area_circle(self):
        self.assertAlmostEqual(area_circle(10), pi*100, delta=0.0001)
        self.assertAlmostEqual(area_circle(0.1), pi * 0.01, delta=0.0001)
        with self.assertRaises(ValueError):
            area_circle(-1)
            area_circle(0)
        with self.assertRaises(TypeError):
            area_circle('10')

    def test_area_rectangle(self):
        self.assertAlmostEqual(area_rectangle(5, 10), 50.00, delta=0.0001)
        self.assertAlmostEqual(area_rectangle(0.5, 10), 5.00, delta=0.0001)
        self.assertAlmostEqual(area_rectangle(5, 0.1), 0.50, delta=0.0001)
        self.assertAlmostEqual(area_rectangle(0.5, 0.4), 0.20, delta=0.0001)
        with self.assertRaises(ValueError):
            area_rectangle(0, 9)
            area_rectangle(8, 0)
            area_rectangle(2, -9)
            area_rectangle(-2, 9)
            area_rectangle(-1, -9)
            area_rectangle(0, 0)
        with self.assertRaises(TypeError):
            area_rectangle('2', 12)
            area_rectangle(2, '12')
            area_rectangle('2', '12')

    def test_area_square(self):
        self.assertAlmostEqual(area_square(10), 100.00, delta=0.0001)
        self.assertAlmostEqual(area_square(0.2), 0.040, delta=0.0001)
        with self.assertRaises(ValueError):
            area_square(0)
            area_square(-5)
        with self.assertRaises(TypeError):
            area_square('4')

    def test_area_triangle(self):
        self.assertAlmostEqual(area_triangle(2, 4), 4.00, delta=0.0001)
        self.assertAlmostEqual(area_triangle(0.4, 5), 1.00, delta=0.0001)
        self.assertAlmostEqual(area_triangle(4, 0.6), 1.20, delta=0.0001)
        self.assertAlmostEqual(area_triangle(0.4, 0.6), 0.12, delta=0.0001)
        with self.assertRaises(ValueError):
            area_triangle(0, 9)
            area_triangle(8, 0)
            area_triangle(2, -9)
            area_triangle(-2, 9)
            area_rectangle(-1, -9)
            area_rectangle(0, 0)
        with self.assertRaises(TypeError):
            area_triangle('2', 12)
            area_triangle(2, '12')
            area_triangle('2', '12')

