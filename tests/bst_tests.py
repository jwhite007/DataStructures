#! /usr/bin/env python

import unittest
from data_structures.bst import Tree

"""Tests for linked_list.py"""


class TestTree(unittest.TestCase):

    def test_insert(self):
        l = []
        tree = buildTree(l)
        tree.insert(8)
        self.assertEqual(8, tree.val)
        self.assertEqual(tree.left, None)
        tree.insert(5)
        tree.insert(20)
        self.assertEqual((8, 5, 20, None, None), (tree.val, tree.left.val,
                         tree.right.val, tree.left.left, tree.right.right))

    def test_contains(self):
        l = [8, 5, 20]
        tree = buildTree(l)
        self.assertFalse(tree.contains(30))
        self.assertTrue(tree.contains(20))
        l = []
        tree = buildTree(l)
        self.assertFalse(tree.contains(8))

    def test_size(self):
        l = [8, 5, 20]
        tree = buildTree(l)
        self.assertEqual(tree.size(), 3)
        tree.insert(40)
        self.assertEqual(tree.size(), 4)
        l = []
        tree = buildTree(l)
        self.assertEqual(tree.size(), 0)

    def test_depth(self):
        l = [8, 5, 20]
        tree = buildTree(l)
        self.assertEqual(tree.depth(), 2)
        tree.insert(40)
        self.assertEqual(tree.depth(), 3)
        l = []
        tree = buildTree(l)
        self.assertEqual(tree.depth(), 0)

    def test_check_balance(self):
        l = [8, 5, 20]
        tree = buildTree(l)
        self.assertEqual(tree.check_balance(), '0 (the tree is balanced)')
        tree.insert(40)
        self.assertEqual(tree.check_balance(),
                         '1 (unbalanced to the right)')
        tree.insert(3)
        tree.insert(2)
        self.assertEqual(tree.check_balance(), '-1 (unbalanced to the left)')

    def test_in_order(self):
        l = [8, 5, 20, 15, 3, 2]
        tree = buildTree(l)
        iol = []
        for node in tree.in_order():
            iol.append(node)
        self.assertListEqual(iol, [2, 3, 5, 8, 15, 20])
        l = []
        tree = buildTree(l)
        iol = []
        for node in tree.in_order():
            iol.append(node)
        self.assertListEqual(iol, [])

    def test_pre_order(self):
        l = [8, 5, 20, 15, 3, 2, 6, 25]
        tree = buildTree(l)
        preol = []
        for node in tree.pre_order():
            preol.append(node)
        print preol
        self.assertListEqual(preol, [8, 5, 3, 2, 6, 20, 15, 25])

    def test_post_order(self):
        l = [8, 5, 20, 15, 3, 2, 6, 25]
        tree = buildTree(l)
        postol = []
        for node in tree.post_order():
            postol.append(node)
        print postol
        self.assertListEqual(postol, [2, 3, 6, 5, 15, 25, 20, 8])

    def test_breadth_first(self):
        l = [8, 5, 20, 15, 3, 2, 6, 25]
        tree = buildTree(l)
        self.assertListEqual(tree.breadth_first(),
                             [8, 5, 20, 3, 6, 15, 25, 2])

    def test_rm_node(self):
        # no descendants
        l = [8, 5, 20]
        tree = buildTree(l)
        tree.rm_node(20)
        iol = []
        for node in tree.in_order():
            iol.append(node)
        self.assertListEqual(iol, [5, 8])

        # one descendant
        l = [8, 5, 20, 30]
        tree = buildTree(l)
        tree.rm_node(20)
        iol = []
        for node in tree.in_order():
            iol.append(node)
        self.assertListEqual(iol, [5, 8, 30])

        # two descendants
        l = [8, 5, 20, 30, 15]
        tree = buildTree(l)
        tree.rm_node(20)
        iol = []
        for node in tree.in_order():
            iol.append(node)
        self.assertListEqual(iol, [5, 8, 15, 30])



def buildTree(l):
    new_Tree = Tree()
    for i in l:
        new_Tree.insert(i)
    return new_Tree

if __name__ == "__main__":
    unittest.main()
