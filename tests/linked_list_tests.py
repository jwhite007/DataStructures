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

    def test_insert_to_empty(self):
        self.linky = linked_list.Linkedlist()
        self.linky.insert(1)
        self.assertEqual(1, self.linky.head.val)

    def test_insert_to_non_empty(self):
        self.linky.insert(5)
        self.assertEqual(5, self.linky.head.val)

    def test_pop_empty(self):
        self.linky = linked_list.Linkedlist()
        self.assertEqual(None, self.linky.pop())

    def test_pop_non_empty(self):
        self.assertEqual(4, self.linky.pop())

    def test_size_greater_than_one(self):
        self.assertEqual(4, self.linky.size())

    def test_size_of_one(self):
        self.linky = linked_list.Linkedlist()
        self.linky.insert(1)
        self.assertEqual(1, self.linky.size())

    def test_size_of_zero(self):
        self.linky = linked_list.Linkedlist()
        self.assertEqual(0, self.linky.size())

    def test_search_exists(self):
        self.assertEqual(3, self.linky.search(3))

    def test_search_not_exists(self):
        self.assertEqual(None, self.linky.search(5))

    def test_remove_head(self):
        self.linky.remove(4)
        self.assertEqual('[3, 2, 1]', self.linky.print_me())

    def test_remove_middle(self):
        self.linky.remove(2)
        self.assertEqual('[4, 3, 1]', self.linky.print_me())

    def test_print_me(self):
        self.linky = linked_list.Linkedlist()
        self.assertEqual('[]', self.linky.print_me())

    def test_print_0th_from_4th(self):
        self.assertEqual(1, self.linky.print_kth_from_nth(0, 4))

    def test_print_1st_from_4th(self):
        self.assertEqual(2, self.linky.print_kth_from_nth(1, 4))

    def test_print_0th_from_2nd(self):
        self.assertEqual(3, self.linky.print_kth_from_nth(0, 2))

    def test_print_1st_from_2nd(self):
        self.assertEqual(4, self.linky.print_kth_from_nth(1, 2))

if __name__ == "__main__":
    unittest.main()
