"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest


class CircleTest(unittest.TestCase):
    """Test Circle"""
    def setUp(self):
        """initial"""
        self.circle = Circle(5)
        self.radius = self.circle.get_radius()
        self.area = self.circle.get_area()

    def test_radius_positive(self):
        """test if radius is positive or zero"""
        self.assertGreaterEqual(self.radius, 0.0)

    def test_add_positive_radius(self):
        """test add positive radius"""
        self.circle.add_area(self.circle)

    def test_add_zero_radius(self):
        self.circle.add_area(Circle(0))
        self.assertEquals(self.circle.get_radius(), self.radius)
        self.assertEquals(self.circle.get_area(), self.area)


if __name__ == '__main__':
    unittest.main()
