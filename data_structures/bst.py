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
            return None
        elif val < self.val:
            if self.left is None:
                self.left = Tree()
            self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Tree()
            self.right.insert(val)

    def contains(self, val):
        if self.val is None:
            return False
        elif val == self.val:
            return True
        elif val < self.val:
            if self.left is None:
                return False
            else:
                return self.left.contains(val)
        elif val > self.val:
            if self.right is None:
                return False
            else:
                return self.right.contains(val)

    def size(self):
        count = 0
        if self.val is not None:
            count += 1
        if self.left is not None:
            count += self.left.size()
        if self.right is not None:
            count += self.right.size()
        return count

    def depth(self):
        if self.val is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return self.right.depth() + 1
        elif self.right is None and self.left is not None:
            return self.left.depth() + 1
        else:
            return max(self.left.depth(), self.right.depth()) + 1

    def check_balance(self):
        diff = self.right.size() - self.left.size()
        if diff > 0:
            return str(diff) + ' (unbalanced to the right)'
        if diff < 0:
            return str(diff) + ' (unbalanced to the left)'
        if diff == 0:
            return str(diff) + ' (the tree is balanced)'

    def _grab_left(self):
        if self.left is None:
            return self.val
        else:
            return self.left._grab_left()

    def _grab_right(self):
        if self.right is None:
            return self.val
        else:
            return self.right._grab_right()

    def rm_node(self, val):
        if self.val == val:
            if self.left is not None:
                self.val = self.left._grab_right()
                self.left = self.left.rm_node(self.val)
                return self
            elif self.right is not None:
                self.val = self.right._grab_left()
                self.right = self.right.rm_node(self.val)
                return self
            else:
                self.val = None
                return None
        else:
            if self.val > val and self.left is not None:
                self.left = self.left.rm_node(val)
            if self.val < val and self.right is not None:
                self.right = self.right.rm_node(val)
            return self

    def in_order(self):
        if self.val is not None:
            if self.left is not None:
                for node in self.left.in_order():
                    yield node
            yield self.val
            if self.right is not None:
                for node in self.right.in_order():
                    yield node

    def pre_order(self):
        if self.val is not None:
            yield self.val
            if self.left is not None:
                for node in self.left.pre_order():
                    yield node
            if self.right is not None:
                for node in self.right.pre_order():
                    yield node

    def post_order(self):
        if self.val is not None:
            if self.left is not None:
                for node in self.left.post_order():
                    yield node
            if self.right is not None:
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
                    # Can change to yeild and get rid of final list.
                    final_list.append(n.val)
                if n.left is not None:
                    next_level.append(n.left)
                if n.right is not None:
                    next_level.append(n.right)
            current_level = next_level
        return final_list

    def printTreeInOrder(tree):

        iol = []
        for node in tree.in_order():
            iol.append(node)
        print iol

if __name__ == '__main__':
    pass
