#! /usr/bin/env python
import queue


class Tree(object):
    """docstring for Tree"""
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

    def insert(self, val):
        if self.val is None:
            self.val = val
            self.left = Tree()
            self.right = Tree()
        elif val < self.val:
            self.left.insert(val)
        elif val > self.val:
            self.right.insert(val)

    def contains(self, val):
        if self.val is None:
            return False
        elif val == self.val:
            return True
        elif val < self.val:
            return self.left.contains(val)
        elif val > self.val:
            return self.right.contains(val)

    def size(self):
        count = 0
        if self.val is not None:
            count += 1
        if self.left.val is not None:
            count += self.left.size()
        if self.right.val is not None:
            count += self.right.size()
        return count

    def depth(self):
        if self.val is None:
            return 0
        return max(self.left.depth(), self.right.depth()) + 1

    def balance(self):
        diff = self.right.size() - self.left.size()
        if diff > 0:
            return str(diff) + ' unbalance to the right'
        if diff < 0:
            return str(diff) + ' unbalance to the left'
        if diff == 0:
            return 'the tree is balanced'

    def rm_node(self, val):
        if self.val is None:
            return False
        if val == self.val:
            temp_list = breadth_first(self)
            temp_list = temp_list[1:]
            self = None
            for node in temp_list:
                self.insert(node)
            return
        elif val == self.left.val:
            temp_list = breadth_first(self.left)
            temp_list = temp_list[1:]
            self.left = None
            for node in temp_list:
                self.insert(node)
            return
        elif val == self.right.val:
            temp_list = breadth_first(self.left)
            self.left = None
            for node in temp_list:
                self.insert(node)
            return
        elif val < self.val:
            return self.left.rm_node(val)
        elif val > self.val:
            return self.right.rm_node(val)


def in_order(tree):
    if tree is not None:
        for node in in_order(tree.left):
            if node is not None:
                yield node
        yield tree.val
        for node in in_order(tree.right):
            if node is not None:
                yield node


def pre_order(tree):
    if tree is not None:
        yield tree.val
        for node in pre_order(tree.left):
            if node is not None:
                yield node
        for node in pre_order(tree.right):
            if node is not None:
                yield node


def post_order(tree):
    if tree is not None:
        for node in post_order(tree.left):
            if node is not None:
                yield node
        for node in post_order(tree.right):
            if node is not None:
                yield node
        yield tree.val


def breadth_first(tree):
    current_level = [tree]
    final_list = []
    while current_level:
        next_level = []
        for n in current_level:
            if n.val is not None:
                final_list.append(n.val)
            if n.left is not None:
                next_level.append(n.left)
            if n.right is not None:
                next_level.append(n.right)
        current_level = next_level
    return final_list


if __name__ == '__main__':
    list1 = [8, 5, 20, 3, 7, 15, 25, 30, 2, 4]
    new_Tree = Tree()
    for i in list1:
        new_Tree.insert(i)
    # print(new_Tree.val)
    # print(new_Tree.contains(8))
    # print(new_Tree.size())
    # print(new_Tree.depth())
    # print(new_Tree.balance())
    iol = []
    for node in in_order(new_Tree):
        iol.append(node)
    print iol
    preol = []
    for node in pre_order(new_Tree):
        preol.append(node)
    print preol
    postol = []
    for node in post_order(new_Tree):
        postol.append(node)
    print postol
    print(breadth_first(new_Tree))
    # print(new_Tree.contains(10))

