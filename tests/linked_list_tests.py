#! /usr/bin/env python

import unittest
from data_structures.linked_list import LinkedList

"""Tests for linked_list.py"""


class TestLinky(unittest.TestCase):

    def setUp(self):
        self.linky = LinkedList()
        l = [1, 2, 3, 4]
        for i in l:
            self.linky.insert(i)

    def test_insert_to_empty(self):
        self.linky = LinkedList()
        self.linky.insert(1)
        self.assertEqual(1, self.linky.head.val)

    def test_insert_to_non_empty(self):
        self.linky.insert(5)
        self.assertEqual(5, self.linky.head.val)

    def test_pop_empty(self):
        self.linky = LinkedList()
        self.assertEqual(None, self.linky.pop())

    def test_pop_non_empty(self):
        self.assertEqual(4, self.linky.pop())

    def test_size_greater_than_one(self):
        self.assertEqual(4, self.linky.size())

    def test_size_of_one(self):
        self.linky = LinkedList()
        self.linky.insert(1)
        self.assertEqual(1, self.linky.size())

    def test_size_of_zero(self):
        self.linky = LinkedList()
        self.assertEqual(0, self.linky.size())

    def test_search_exists(self):
        self.assertEqual(True, self.linky.search(3))

    def test_search_not_exists(self):
        self.assertEqual(False, self.linky.search(5))

    def test_remove_head(self):
        self.linky.remove(4)
        self.assertListEqual([3, 2, 1], self.linky.print_me())

    def test_remove_middle(self):
        self.linky.remove(2)
        self.assertListEqual([4, 3, 1], self.linky.print_me())

    def test_print_me(self):
        self.linky = LinkedList()
        self.assertListEqual([], self.linky.print_me())

    def test_print_0th_from_4th(self):
        self.assertEqual(1, self.linky.print_kth_from_nth(0, 4))

    def test_print_1st_from_4th(self):
        self.assertEqual(2, self.linky.print_kth_from_nth(1, 4))

    def test_print_0th_from_2nd(self):
        self.assertEqual(3, self.linky.print_kth_from_nth(0, 2))

    def test_print_1st_from_2nd(self):
        self.assertEqual(4, self.linky.print_kth_from_nth(1, 2))

    def test_partition_around_x(self):
        self.linky = LinkedList()
        l = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9, 10]
        for i in range(len(l)):
            self.linky.insert(l[i])
        self.linky.partition_around_x(5)
        self.assertListEqual([1, 2, 3, 4, 5, 5, 10, 9, 8, 7, 6],
                             self.linky.print_me())

    def test_rem_dups(self):
        self.linky = LinkedList()
        self.linky.insert(1)
        self.linky.insert(1)
        self.linky.insert(2)
        self.linky.insert(2)
        self.linky.insert(3)
        self.linky.insert(3)
        self.linky.rem_dups()
        self.assertListEqual([3, 2, 1], self.linky.print_me())

if __name__ == "__main__":
    unittest.main()
