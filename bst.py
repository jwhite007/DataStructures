#! /usr/bin/env python

from math import ceil
from math import log


class Node(object):
    """docstring for Node"""
    def __init__(self, val):
        super(Node, self).__init__()
        self.left = None
        self.right = None
        self.val = val


class BST(object):
    """docstring for BST"""
    def __init__(self):
        super(BST, self).__init__()
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        elif new_node.val < self.root.val:
            if self.root.left is None:
                self.root.left = BST()
            self.root.left.insert(new_node.val)
        elif new_node.val > self.root.val:
            if self.root.right is None:
                self.root.right = BST()
            self.root.right.insert(new_node.val)

    def contains(self, val):
        if self.root is None:
            return False
        elif val == self.root.val:
            return True
        elif val < self.root.val:
            if self.root.left is None:
                return False
            else:
                return self.root.left.contains(val)
        elif val > self.root.val:
            if self.root.right is None:
                return False
            else:
                return self.root.right.contains(val)

    def size(self):
        count = 0
        if self.root is not None:
            count += 1
        if self.root.left is not None:
            count += self.root.left.size()
        if self.root.right is not None:
            count += self.root.right.size()
        return count

    def count_nones(self):
        count = 0
        if self.root.left is None:
            count += 1
        else:
            count += self.root.left.count_nones()
        if self.root.right is None:
            count += 1
        else:
            count += self.root.right.count_nones()
        return count

    def depth(self):

        # count = 0
        # if self.root is not None:
        #     count += 1
        #     if self.root.left is not None and self.root.right is not None:
        #     if self.root.left.size() > self.root.right.size():
        #         self.root.left.depth()
        #     else:
        #         self.root.right.depth()

    def balance():
        pass


if __name__ == '__main__':
    list1 = [5, 6, 4, 8]
    new_BST = BST()
    for i in list1:
        new_BST.insert(i)
    print(new_BST.root.val)
    # print(new_BST.count)
    print(new_BST.root.left.root.val)
    # print(new_BST.count)
    print(new_BST.root.right.root.val)
    print(new_BST.root.right.root.right.root.val)
    print(new_BST.contains(8))
    print(new_BST.size())
    print(new_BST.count_nones())
    # print(new_BST.depth())
    # print(new_BST.contains(10))


