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
            # self.left = Tree()
            # self.right = Tree()
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
            return self.left.contains(val)
        elif val > self.val:
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

    def balance(self):
        diff = self.right.size() - self.left.size()
        if diff > 0:
            return str(diff) + ' (unbalanced to the right)'
        if diff < 0:
            return str(diff) + ' (unbalanced to the left)'
        if diff == 0:
            return str(diff) + ' (the tree is balanced)'

    def _grab_left(self):
        if self.right is None:
            return self.val
        else:
            self.left._grab_left()

    def _grab_right(self):
        if self.right is None:
            return self.val
        else:
            self.right._grab_right()

    def rm_node(self, val):
        if self.val == val:
            if self.left is not None:
            # if self.left.size() >= self.right.size() and self.left is not None:
                self.val = self.left._grab_right()
                self.left.rm_node(self.val)
            elif self.right is not None:
            # elif self.right.size() > self.left.size():
                self.val = self.right._grab_left()
                self.right.rm_node(self.val)
            else:
                self.val is None
        else:
            if self.val > val and self.left is not None:
                return self.left.rm_node(val)
            elif self.val < val and self.right is not None:
                return self.right.rm_node(val)
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
    print(new_Tree.val)
    print(new_Tree.contains(8))
    print(new_Tree.size())
    print(new_Tree.depth())
    print(new_Tree.balance())
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
    mod_Tree = new_Tree.rm_node(5)
    iol = []
    for node in mod_Tree.in_order():
        iol.append(node)
    print iol

    # print(new_Tree.contains(10))

