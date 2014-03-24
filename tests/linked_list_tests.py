#! /usr/bin/env python

import unittest
from data_structures import linked_list

"""Tests for linked_list.py"""


class TestLinky(unittest.TestCase):

    def setUp(self):
        self.linky = linked_list.Linkedlist()
        self.linky.insert(1)
        self.linky.insert(2)
        self.linky.insert(3)
        self.linky.insert(4)

    def testInsertToEmpty(self):
        self.linky = linked_list.Linkedlist()
        self.linky.insert(1)
        self.assertEqual(1, self.linky.head.val)

    def testInsertToNonEmpty(self):
        self.setUp()
        self.linky.insert(5)
        self.assertEqual(5, self.linky.head.val)

    def testPopEmpty(self):
        self.linky = linked_list.Linkedlist()
        self.assertEqual(None, self.linky.pop())

    def testPopNonEmpty(self):
        self.setUp()
        self.assertEqual(4, self.linky.pop())

    def testSizeGthanOne(self):
        self.setUp()
        self.assertEqual(4, self.linky.size())

    def testSizeAtOne(self):
        self.linky = linked_list.Linkedlist()
        self.linky.insert(1)
        self.assertEqual(1, self.linky.size())

    def testSizeAtZero(self):
        self.linky = linked_list.Linkedlist()
        self.assertEqual(0, self.linky.size())

    def testSearchExists(self):
        self.setUp()
        self.assertEqual(3, self.linky.search(3))

    def testSearchNotExists(self):
        self.setUp()
        self.assertEqual(None, self.linky.search(5))

    def testRemoveHead(self):
        self.setUp()
        self.linky.remove(4)
        self.assertEqual('[3, 2, 1]', self.linky.print_me())

    def testRemoveMiddle(self):
        self.setUp()
        self.linky.remove(2)
        self.assertEqual('[4, 3, 1]', self.linky.print_me())

    def testPrint_me(self):
        self.linky = linked_list.Linkedlist()
        self.assertEqual('[]', self.linky.print_me())

if __name__ == "__main__":
    unittest.main()
