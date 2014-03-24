#! /usr/bin/env python

import unittest
from data_structures.insort import insort


class TestInSort(unittest.TestCase):
    def test_insort(self):
        l = [8, 4, 5, 20, 6, 2, 15, 1, 30]
        insort(l)
        self.assertListEqual(l, [1, 2, 4, 5, 6, 8, 15, 20, 30])
        l = [8]
        insort(l)
        self.assertListEqual(l, [8])
        l = []
        self.assertListEqual(l, [])
        with self.assertRaises(ValueError):
            insort(1)

if __name__ == "__main__":
    unittest.main()
