#! /usr/bin/env python


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

    def grab_left_node():
        if self.val is not None:
            if self.left.val is None and self.right.val is None
                yeild self.left
            else:
                self.left.grab_left_node()

    def rm_node(self, val):
        if self.val == val:
            if self.left.size() > self.right.size():


    def in_order(self):
        if self.val is not None:
            for node in self.left.in_order():
                yield node
            yield self.val
            for node in self.right.in_order():
                yield node

    def pre_order(self):
        if self.val is not None:
            yield self.val
            for node in self.left.pre_order():
                yield node
            for node in self.right.pre_order():
                yield node

    def post_order(self):
        if self.val is not None:
            for node in self.left.post_order():
                yield node
            for node in self.right.post_order():
                yield node
            yield self.val

    def breadth_first(self):
        current_level = [self]
        final_list = []
        while current_level:
            next_level = []
            for n in current_level:
                if n.val is not None:
                    final_list.append(n.val)  # Can change to yeild and get rid of final list.
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
    for node in new_Tree.in_order():
        iol.append(node)
    print iol
    preol = []
    for node in new_Tree.pre_order():
        preol.append(node)
    print preol
    postol = []
    for node in new_Tree.post_order():
        postol.append(node)
    print postol
    print(new_Tree.breadth_first())
    # print(new_Tree.contains(10))

