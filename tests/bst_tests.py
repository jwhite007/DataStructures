#! /usr/bin/env python

import unittest
from data_structures.bst import Tree

"""Tests for linked_list.py"""


class TestTree(unittest.TestCase):

    def test_insert(self):
        alist = []
        tree = build_tree(alist)
        tree[8] = 'black'
        self.assertEqual('black', tree.val)
        self.assertEqual(8, tree.key)
        self.assertEqual(tree.left, None)
        tree[5] = 'yellow'
        tree[20] = 'blue'
        self.assertEqual((8, 5, 20, None, None), (tree.key, tree.left.key,
                         tree.right.key, tree.left.left, tree.right.right))
        self.assertEqual(('black', 'yellow', 'blue', None, None), (tree.val, tree.left.val,
                         tree.right.val, tree.left.left, tree.right.right))

    def test_contains(self):
        alist = [(8, 'black'), (5, 'yellow'), (20, 'blue')]
        tree = build_tree(alist)
        self.assertFalse(30 in tree)
        self.assertTrue(20 in tree)
        alist = []
        tree = build_tree(alist)
        self.assertFalse(8 in tree)

    def test_size(self):
        alist = [(8, 'black'), (5, 'yellow'), (20, 'blue')]
        tree = build_tree(alist)
        self.assertEqual(tree.size, 3)
        tree[40] = 'brown'
        self.assertEqual(tree.size, 4)
        alist = []
        tree = build_tree(alist)
        self.assertEqual(tree.size, 0)

    def test_height(self):
        alist = [(8, 'black'), (5, 'yellow'), (20, 'blue')]
        tree = build_tree(alist)
        self.assertEqual(tree.height(), 1)
        tree[40] = 'brown'
        self.assertEqual(tree.height(), 2)
        tree[50] = 'orange'
        tree[80] = 'green'
        self.assertEqual(tree.height(), 4)
        tree[6] = 'white'
        self.assertEqual(tree.height(), 4)
        alist = []
        tree = build_tree(alist)
        self.assertEqual(tree.height(), -1)

    def test_get_balance_factor(self):
        alist = [(8, 'black'), (5, 'yellow'), (20, 'blue')]
        tree = build_tree(alist)
        self.assertEqual(tree.get_balance_factor(), 0)
        tree[40] = 'brown'
        self.assertEqual(tree.get_balance_factor(), -1)
        tree[3] = 'orange'
        tree[2] = 'green'
        self.assertEqual(tree.get_balance_factor(), 1)

    def test_in_order(self):
        alist = [(8, 'black'), (5, 'yellow'),
                 (20, 'blue'), (15, 'brown'),
                 (3, 'orange'), (2, 'green'),
                 (6, 'white'), (25, 'gold')]
        tree = build_tree(alist)
        self.assertListEqual(list(tree.in_order()), [(2, 'green'),
                                                     (3, 'orange'),
                                                     (5, 'yellow'),
                                                     (6, 'white'),
                                                     (8, 'black'),
                                                     (15, 'brown'),
                                                     (20, 'blue'),
                                                     (25, 'gold')])
        alist = []
        tree = build_tree(alist)
        self.assertListEqual(list(tree.in_order()), [])

    def test_pre_order(self):
        alist = [(8, 'black'), (5, 'yellow'),
                 (20, 'blue'), (15, 'brown'),
                 (3, 'orange'), (2, 'green'),
                 (6, 'white'), (25, 'gold')]
        tree = build_tree(alist)
        self.assertListEqual(list(tree.pre_order()), [(8, 'black'),
                                                      (5, 'yellow'),
                                                      (3, 'orange'),
                                                      (2, 'green'),
                                                      (6, 'white'),
                                                      (20, 'blue'),
                                                      (15, 'brown'),
                                                      (25, 'gold')])

    def test_post_order(self):
        alist = [(8, 'black'), (5, 'yellow'),
                 (20, 'blue'), (15, 'brown'),
                 (3, 'orange'), (2, 'green'),
                 (6, 'white'), (25, 'gold')]
        tree = build_tree(alist)
        self.assertListEqual(list(tree.post_order()), [(2, 'green'),
                                                       (3, 'orange'),
                                                       (6, 'white'),
                                                       (5, 'yellow'),
                                                       (15, 'brown'),
                                                       (25, 'gold'),
                                                       (20, 'blue'),
                                                       (8, 'black')])

    def test_breadth_first(self):
        alist = [(8, 'black'), (5, 'yellow'),
                 (20, 'blue'), (15, 'brown'),
                 (3, 'orange'), (2, 'green'),
                 (6, 'white'), (25, 'gold')]
        tree = build_tree(alist)
        self.assertListEqual(list(tree.breadth_first()),
                             [(8, 'black'),
                              (5, 'yellow'),
                              (20, 'blue'),
                              (3, 'orange'),
                              (6, 'white'),
                              (15, 'brown'),
                              (25, 'gold'),
                              (2, 'green')])

    def test_rm_node(self):
        # no descendants
        alist = [(8, 'black'), (5, 'yellow'), (20, 'blue')]
        tree = build_tree(alist)
        del tree[20]
        self.assertListEqual(list(tree.in_order()),
                             [(5, 'yellow'), (8, 'black')])

        # one descendant
        alist = [(8, 'black'), (5, 'yellow'), (20, 'blue'), (25, 'gold')]
        tree = build_tree(alist)
        del tree[20]
        self.assertListEqual(list(tree.in_order()),
                             [(5, 'yellow'), (8, 'black'), (25, 'gold')])

        # two descendants
        alist = [(8, 'black'), (5, 'yellow'),
                 (20, 'blue'), (25, 'gold'),
                 (15, 'brown')]
        tree = build_tree(alist)
        del tree[20]
        self.assertListEqual(list(tree.in_order()),
                             [(5, 'yellow'), (8, 'black'),
                              (15, 'brown'), (25, 'gold')])


def build_tree(alist):
    new_tree = Tree()
    for i in alist:
        new_tree[i[0]] = i[1]
    return new_tree

if __name__ == "__main__":
    unittest.main()
