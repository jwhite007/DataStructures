#! /usr/bin/env python

import unittest
from data_structures import mylib


class TestMylib(unittest.TestCase):
    # def setUp(self):
        # self.janTwoTwelve = self.mylib.make_month(2012, 01)
    def test_day_in_month(self):
        janTwoTwelve = mylib.make_month(2012, 01)
        febTwoEleven = mylib.make_month(2011, 02)
        marTwoTen = mylib.make_month(2010, 03)
        self.assertEqual(janTwoTwelve(12), 'Th')
        self.assertEqual(febTwoEleven(16), 'We')
        self.assertEqual(marTwoTen(30), 'Tu')

    def test_day_not_in_month(self):
        febTwoEleven = mylib.make_month(2011, 02)
        febTwoTwelve = mylib.make_month(2012, 02)
        with self.assertRaises(ValueError):
            febTwoEleven(29)
        with self.assertRaises(ValueError):
            febTwoTwelve(30)


if __name__ == "__main__":
    unittest.main()
