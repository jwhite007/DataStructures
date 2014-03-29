#! /usr/bin/env python

import unittest
from data_structures import linked_list

"""Tests for linked_list.py"""


class TestLinky(unittest.TestCase):

    def setUp(self):
        self.linky = linked_list.Linkedlist()
        l = [1, 2, 3, 4]
        for i in l:
            self.linky.insert(i)

    def testInsertToEmpty(self):
        self.linky = linked_list.Linkedlist()
        self.linky.insert(1)
        self.assertEqual(1, self.linky.head.val)

    def testInsertToNonEmpty(self):
        self.linky.insert(5)
        self.assertEqual(5, self.linky.head.val)

    def testPopEmpty(self):
        self.linky = linked_list.Linkedlist()
        self.assertEqual(None, self.linky.pop())

    def testPopNonEmpty(self):
        self.assertEqual(4, self.linky.pop())

    def testSizeGthanOne(self):
        self.assertEqual(4, self.linky.size())

    def testSizeAtOne(self):
        self.linky = linked_list.Linkedlist()
        self.linky.insert(1)
        self.assertEqual(1, self.linky.size())

    def testSizeAtZero(self):
        self.linky = linked_list.Linkedlist()
        self.assertEqual(0, self.linky.size())

    def testSearchExists(self):
        self.assertEqual(3, self.linky.search(3))

    def testSearchNotExists(self):
        self.assertEqual(None, self.linky.search(5))

    def testRemoveHead(self):
        self.linky.remove(4)
        self.assertEqual('[3, 2, 1]', self.linky.print_me())

    def testRemoveMiddle(self):
        self.linky.remove(2)
        self.assertEqual('[4, 3, 1]', self.linky.print_me())

    def testPrint_me(self):
        self.linky = linked_list.Linkedlist()
        self.assertEqual('[]', self.linky.print_me())

    def testPrint_0th_from_4th(self):
        self.assertEqual(1, self.linky.print_kth_from_nth(0, 4))

    def testPrint_1st_from_4th(self):
        self.assertEqual(2, self.linky.print_kth_from_nth(1, 4))

    def testPrint_0th_from_2nd(self):
        self.assertEqual(3, self.linky.print_kth_from_nth(0, 2))

    def testPrint_1st_from_2nd(self):
        self.assertEqual(4, self.linky.print_kth_from_nth(1, 2))

if __name__ == "__main__":
    unittest.main()
