import unittest
from circle import circle_draw
from math import pi

class TestCircleDraw(unittest.TestCase):
    def test_draw(self):
        self.assertAlmostEqual(circle_draw(1), pi)
        self.assertAlmostEqual(circle_draw(0), 0)
        self.assertAlmostEqual(circle_draw(2.1), pi*2.1**2)

    def test_values(self):
        self.assertRaises(ValueError, circle_draw, -2)

    def test_types(self):
        self.assertRaises(TypeError, circle_draw, 2+5j)
        self.assertRaises(TypeError, circle_draw, True)
        self.assertRaises(TypeError, circle_draw, "radius")