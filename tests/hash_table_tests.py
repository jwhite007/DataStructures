#! /usr/bin/env python

import unittest
import hash_table


class TestHashTable(unittest.TestCase):

    def test_set_to_empty(self):
        my_ht = hash_table.HashTable(10)
        my_ht.set('puck', 20)
        self.assertEqual(20, my_ht.get('puck'))

    def test_set_nonstring(self):
        my_ht = hash_table.HashTable(10)
        self.assertEqual('key must be a string!', my_ht.set(2, 30))

    def test_get(self):
        my_ht = hash_table.HashTable(10)
        my_ht.set('puck', 20)
        self.assertEqual(20, my_ht.get('puck'))

    def test_get_nonstring(self):
        my_ht = hash_table.HashTable(10)
        self.assertEqual('key must be a string!', my_ht.get(4))

    def test_collision(self):
        my_ht = hash_table.HashTable(10)
        my_ht.set('puck', 20)
        my_ht.set('uckp', 30)
        self.assertEqual(30, my_ht.get('uckp'))

    def test_nonkey(self):
        my_ht = hash_table.HashTable(10)
        my_ht.set('puck', 20)
        self.assertEqual('key is not in table', my_ht.get('python'))

    def test_key_reuse(self):
        my_ht = hash_table.HashTable(10)
        my_ht.set('puck', 20)
        self.assertEqual('key already in use', my_ht.set('puck', 30))

if __name__ == "__main__":
    unittest.main()
