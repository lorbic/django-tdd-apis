from django.test import TestCase

from app.calc import add, sub


class CalcTests(TestCase):

    def test_add_numbers(self):
        "Test that two number are added togerther"
        self.assertEqual(add(3, 8), 11)
        self.assertEqual(add(-3, -8), -11)
    
    def test_subtract_numbers(self):
        """Test that the first number is subtracted from second number"""
        self.assertEqual(sub(3, 8), 5)
        self.assertEqual(sub(-5, 5), 10)

   