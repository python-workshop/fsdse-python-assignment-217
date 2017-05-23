from unittest import TestCase


class TestBuild(TestCase):
    #check wheter  the arrays are declare
    #check if define array are not an array
    #check if defined array are sorted
    #check if defined array mereged or not

    def test_check_wheter_array_are_declare(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result = build(None)
        self.assertEqual(False,result)

    def test_check_if_defined_value_not_an_array(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result = build([])
        self.assertEqual(False,result)

    def test_if_defined_array_are_sorted(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result = build([(1,2),(13,14),(9,7)])
        self.assertEqual([(1,2),(9,7),(13,14)],result)

    def test_if_defined_array_mereged_or_not(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result = build([(1,23),(0,14)])
        self.assertEqual([(0,23)], result)