#! /usr/bin/env python

import unittest
from data_structures.rsort import rsort


class TestRSort(unittest.TestCase):
    def test_rsort(self):
        l1 = [8, 4, 5, 20, 6, 2, 15, 1, 30]
        l2 = rsort(l1, 10)
        self.assertListEqual(l2, [1, 2, 4, 5, 6, 8, 15, 20, 30])
        l1 = [8]
        l2 = rsort(l1, 10)
        self.assertListEqual(l2, [8])
        l1 = []
        l2 = rsort(l1, 10)
        self.assertListEqual(l2, [])
        with self.assertRaises(ValueError):
            rsort(1, 10)

if __name__ == "__main__":
    unittest.main()
