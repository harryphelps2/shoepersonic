from django.test import TestCase
from .models import Shoe

class ShoeTests(TestCase):
    """
    Tests for Shoe model.
    """
    def test_str(self):
        testname = Shoe(name="Super fast shoe")
        self.assertEqual(str(testname), "Super fast shoe")
