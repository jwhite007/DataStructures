#! /usr/bin/env python
from Queue import Queue


class Tree(object):
    """docstring for Tree"""
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None
        self.key = None
        self.size = 0

    def insert(self, key, val):
        if self.key is None:
            self.key = key
            self.val = val
            self.size += 1
            return None
        elif key < self.key:
            if self.left is None:
                self.left = Tree()
            self.left.insert(key, val)
            self.size += 1
        elif key > self.key:
            if self.right is None:
                self.right = Tree()
            self.right.insert(key, val)
            self.size += 1
        elif key == self.key:
            msg = 'key already in tree'
            raise ValueError(msg)

    def __setitem__(self, key, val):
        return self.insert(key, val)

    def ret_val(self, key):
        if self.key is None:
            return 'key is not in tree'
        elif key == self.key:
            return self.val
        elif key < self.key:
            if self.left is None:
                return 'key is not in tree'
            else:
                return self.left.ret_val(key)
        elif key > self.key:
            if self.right is None:
                return 'key is not in tree'
            else:
                return self.right.ret_val(key)

    def __getitem__(self, key):
        return self.ret_val(key)

    def contains(self, key):
        if self.key is None:
            return False
        elif key == self.key:
            return True
        elif key < self.key:
            if self.left is None:
                return False
            else:
                return self.left.contains(key)
        elif key > self.key:
            if self.right is None:
                return False
            else:
                return self.right.contains(key)

    def __contains__(self, key):
        return self.contains(key)

    # def size(self):
    #     count = 0
    #     if self.key is not None:
    #         count += 1
    #     if self.left is not None:
    #         count += self.left.size()
    #     if self.right is not None:
    #         count += self.right.size()
    #     return count

    def height(self):
        if self.key is None:
            return -1
        elif self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return self.right.height() + 1
        elif self.right is None:
            return self.left.height() + 1
        else:
            return max(self.left.height(), self.right.height()) + 1

    def get_balance_factor(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return -self.right.height() - 1
        elif self.right is None:
            return self.left.height() + 1
        else:
            return self.left.height() - self.right.height()

    def __grab_left(self):
        if self.left is None:
            return self.key, self.val
        else:
            return self.left.__grab_left()

    def __grab_right(self):
        if self.right is None:
            return self.key, self.val
        else:
            return self.right.__grab_right()

    def rm_node(self, key):
        if self.key == key:
            if self.left is not None:
                self.key, self.val = self.left.__grab_right()
                self.left = self.left.rm_node(self.key)
                self.size -= 1
                return self
            elif self.right is not None:
                self.key, self.val = self.right.__grab_left()
                self.right = self.right.rm_node(self.key)
                self.size -= 1
                return self
            else:
                self.key = None
                self.val = None
                self.size -= 1
                return None
        else:
            if self.key > key and self.left is not None:
                self.left = self.left.rm_node(key)
            if self.key < key and self.right is not None:
                self.right = self.right.rm_node(key)
            self.size -= 1
            return self

    def __delitem__(self, key):
        return self.rm_node(key)

    def in_order(self):
        if self.key is not None:
            if self.left is not None:
                for node in self.left.in_order():
                    yield node
            yield self.key, self.val
            if self.right is not None:
                for node in self.right.in_order():
                    yield node

    def pre_order(self):
        if self.key is not None:
            yield self.key, self.val
            if self.left is not None:
                for node in self.left.pre_order():
                    yield node
            if self.right is not None:
                for node in self.right.pre_order():
                    yield node

    def post_order(self):
        if self.key is not None:
            if self.left is not None:
                for node in self.left.post_order():
                    yield node
            if self.right is not None:
                for node in self.right.post_order():
                    yield node
            yield self.key, self.val

    def breadth_first(self):
        current_level = [self]
        while current_level:
            next_level = []
            for node in current_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
                if node.key is not None:
                    yield node.key, node.val
            current_level = next_level

    def breadth_first_queue(self):
        current_level = Queue()
        current_level.put(self)
        while not current_level.empty():
            current_node = current_level.get()
            if current_node.left is not None:
                current_level.put(current_node.left)
            if current_node.right is not None:
                current_level.put(current_node.right)
            if current_node.key is not None:
                yield current_node.key, current_node.val

    # def balance(self):
    #     if self.get_balance_factor() >
    def switch_to_right(self):
        self.right = self


class Node(object):
    """docstring for Node"""
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right_child = None
        self.left_child = None
        self.parent = None
        self.balance_factor = 0

    def set_balance_factor(self):
        if self.left_child is None and self.right_child is None:
            self.balance_factor = 0
        elif self.left_child is None:
            self.balance_factor = -self.right_child.height() - 1
        elif self.right_child is None:
            self.balance_factor = self.left_child.height() + 1
        else:
            self.balance_factor = self.left_child.height() - self.right_child.height()

    def height(self):
        if self.left_child is None and self.right_child is None:
            return 0
        elif self.left_child is None:
            return self.right_child.height() + 1
        elif self.right_child is None:
            return self.left_child.height() + 1
        else:
            return max(self.left_child.height(), self.right_child.height()) + 1

    def get_balance_factor(self):
        return self.balance_factor

    # def get_balance_factor(self):
    #     if self.left_child is None and self.right_child is None:
    #         return 0
    #     elif self.left_child is None:
    #         return -self.right_child.height() - 1
    #     elif self.right_child is None:
    #         return self.left_child.height() + 1
    #     else:
    #         return self.left_child.height() - self.right_child.height()


class TreeWithNodes(object):
    """docstring for TreeWithNodes"""
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, val):
        # import pdb
        # pdb.set_trace()
        if self.root is None:
            self.root = Node(key, val)
            self.size += 1
        else:
            current_node = self.root
            new_node = Node(key, val)
            self._put(key, val, current_node, new_node)

    # def _put(self, key, val, current_node, new_node):
    #     if new_node.key < current_node.key:
    #         if current_node.left_child is None:
    #             (current_node.left_child,
    #              new_node.parent) = (new_node,
    #                                  current_node)
    #             self.size += 1
    #         else:
    #             return self._put(key, val, current_node.left_child, new_node)
    #     elif new_node.key > current_node.key:
    #         if current_node.right_child is None:
    #             (current_node.right_child,
    #              new_node.parent) = (new_node,
    #                                  current_node)
    #             self.size += 1
    #         else:
    #             return self._put(key, val, current_node.right_child, new_node)
    #     else:
    #         current_node.val = new_node.val

    def _put(self, key, val, current_node, new_node):
        if new_node.key < current_node.key:
            if current_node.left_child is None:
                (current_node.left_child,
                 new_node.parent) = (new_node,
                                     current_node)
                self.size += 1
                self.put_update_balance_factor(current_node.left_child)
            else:
                return self._put(key, val, current_node.left_child, new_node)
        elif new_node.key > current_node.key:
            if current_node.right_child is None:
                (current_node.right_child,
                 new_node.parent) = (new_node,
                                     current_node)
                self.size += 1
                self.put_update_balance_factor(current_node.right_child)
            else:
                return self._put(key, val, current_node.right_child, new_node)
        else:
            current_node.val = new_node.val

    def put_update_balance_factor(self, update_node):
        if update_node.parent is not None:
            if update_node.parent.left_child == update_node:
                update_node.parent.balance_factor += 1
            else:
                update_node.parent.balance_factor -= 1
            if update_node.parent.balance_factor != 0:
                self.put_update_balance_factor(update_node.parent)

    def __setitem__(self, key, val):
        return self.put(key, val)

    def ret_val(self, key):
        if self.root is None:
            return None
        else:
            current_node = self.root
            return self._ret_val(key, current_node)

    def _ret_val(self, key, current_node):
        if key == current_node.key:
            return current_node.val
        elif key < current_node.key:
            if current_node.left_child is None:
                return None
            else:
                return self._ret_val(key, current_node.left_child)
        else:
            if current_node.right_child is None:
                return None
            else:
                return self._ret_val(key, current_node.right_child)

    def __getitem__(self, key):
        return self.ret_val(key)

    def contains(self, key):
        current_node = self.root
        return self._contains(key, current_node)

    def _contains(self, key, current_node):
        if key == current_node.key:
            return True
        elif key < current_node.key:
            if current_node.left_child is None:
                return False
            else:
                return self._contains(key, current_node.left_child)
        else:
            if current_node.right_child is None:
                return False
            else:
                return self._contains(key, current_node.right_child)

    def __contains__(self, key):
        return self.contains(key)

    def height(self):
        return self.root.height()

    def rm_node(self, key):
        if self.root is None:
            raise KeyError
        current_node = self.root
        return self._rm_node(key, current_node)

    def __delitem__(self, key):
        return self.rm_node(key)

    # def _rm_node(self, key, current_node):
    #     if key == current_node.key:
    #         if current_node.left_child is None and current_node.right_child is None:
    #             if current_node == self.root:
    #                 self.root = None
    #             else:
    #                 if current_node.parent.left_child == current_node:
    #                     current_node.parent.left_child = None
    #                 else:
    #                     current_node.parent.right_child = None
    #         else:
    #             if current_node.get_balance_factor() >= 0:
    #                 if current_node.left_child.right_child is None:
    #                     replacement_node = current_node.left_child
    #                     current_node.left_child = replacement_node.left_child
    #                 else:
    #                     replacement_node = self._grab_right(current_node.left_child)
    #                     replacement_node.parent.right_child = replacement_node.left_child
    #             else:
    #                 if current_node.right_child.left_child is None:
    #                     replacement_node = current_node.right_child
    #                     current_node.right_child = replacement_node.right_child
    #                 else:
    #                     replacement_node = self._grab_left(current_node.right_child)
    #                     replacement_node.parent.left_child = replacement_node.right_child
    #             replacement_node.left_child = current_node.left_child
    #             replacement_node.right_child = current_node.right_child
    #             if current_node == self.root:
    #                 self.root = replacement_node
    #             else:
    #                 replacement_node.parent = current_node.parent
    #                 if current_node.parent.left_child == current_node:
    #                     current_node.parent.left_child = replacement_node
    #                 else:
    #                     current_node.parent.right_child = replacement_node
    #         self.size -= 1

    def _rm_node(self, key, current_node):
        if key == current_node.key:
            update_node = None
            if current_node.left_child is None and current_node.right_child is None:
                if current_node == self.root:
                    self.root = None
                else:
                    if current_node.parent.left_child == current_node:
                        current_node.parent.left_child = None
                        current_node.parent.balance_factor -= 1
                    else:
                        current_node.parent.right_child = None
                        current_node.parent.balance_factor += 1
                    update_node = current_node.parent
            else:
                if current_node.get_balance_factor() >= 0:
                    if current_node.left_child.right_child is None:
                        replacement_node = current_node.left_child
                        current_node.left_child = replacement_node.left_child
                        if current_node != self.root:
                            if current_node.parent.left_child == current_node:
                                current_node.parent.left_child = replacement_node
                            else:
                                current_node.parent.right_child = replacement_node
                        replacement_node.balance_factor = current_node.balance_factor - 1
                        update_node = replacement_node
                    else:
                        replacement_node = self._grab_right(current_node.left_child)
                        replacement_node.parent.right_child = replacement_node.left_child
                        replacement_node.parent.balance_factor += 1
                        if replacement_node.left_child is not None:
                            replacement_node.left_child.parent = replacement_node.parent
                        replacement_node.left_child = current_node.left_child
                        if replacement_node.left_child is not None:
                            replacement_node.left_child.parent = replacement_node
                        replacement_node.right_child = current_node.right_child
                        if replacement_node.right_child is not None:
                            replacement_node.right_child.parent = replacement_node
                        if current_node != self.root:
                            if current_node.parent.left_child == current_node:
                                current_node.parent.left_child = replacement_node
                            else:
                                current_node.parent.right_child = replacement_node
                        replacement_node.balance_factor = current_node.balance_factor
                        update_node = replacement_node.parent
                else:
                    if current_node.right_child.left_child is None:
                        replacement_node = current_node.right_child
                        current_node.right_child = replacement_node.right_child
                        if current_node != self.root:
                            if current_node.parent.left_child == current_node:
                                current_node.parent.left_child = replacement_node
                            else:
                                current_node.parent.right_child = replacement_node
                        replacement_node.balance_factor = current_node.balance_factor + 1
                        update_node = replacement_node
                    else:
                        replacement_node = self._grab_left(current_node.right_child)
                        replacement_node.parent.left_child = replacement_node.right_child
                        replacement_node.parent.balance_factor -= 1
                        if replacement_node.parent.left_child is not None:
                            replacement_node.parent.right_child.parent = replacement_node.parent
                        replacement_node.left_child = current_node.left_child
                        if replacement_node.left_child is not None:
                            replacement_node.left_child.parent = replacement_node
                        replacement_node.right_child = current_node.right_child
                        if replacement_node.right_child is not None:
                            replacement_node.right_child.parent = replacement_node
                        if current_node != self.root:
                            if current_node.parent.left_child == current_node:
                                current_node.parent.left_child = replacement_node
                            else:
                                current_node.parent.right_child = replacement_node
                        replacement_node.balance_factor = current_node.balance_factor
                        update_node = replacement_node.parent
                if current_node == self.root:
                    self.root = replacement_node
                else:
                    replacement_node.parent = current_node.parent
                    if current_node.parent.left_child == current_node:
                        current_node.parent.left_child = replacement_node
                    else:
                        current_node.parent.right_child = replacement_node
            self.size -= 1
            self.remove_update_balance_factor(update_node)

        elif key < current_node.key:
            if current_node.left_child is None:
                raise KeyError
            self._rm_node(key, current_node.left_child)
        else:
            if current_node.right_child is None:
                raise KeyError
            self._rm_node(key, current_node.right_child)

    def remove_update_balance_factor(self, update_node):
        if update_node.balance_factor == 0:
            if update_node.parent is not None:
                if update_node.parent.left_child == update_node:
                    update_node.parent.balance_factor -= 1
                else:
                    update_node.parent.balance_factor += 1
                self.remove_update_balance_factor(update_node.parent)

    def _grab_right(self, current_node):
        if current_node.right_child is None:
            return current_node
        return self._grab_right(current_node.right_child)

    def _grab_left(self, current_node):
        if current_node.left_child is None:
            return current_node
        return self._grab_left(current_node.left_child)

    def get_balance_factor(self):
        if self.root is None:
            return None
        return self.root.get_balance_factor()

    def in_order(self):
        if self.root is None:
            return [None]
        current_node = self.root
        return self._in_order(current_node)

    def _in_order(self, current_node):
        if current_node.left_child is not None:
            for node in self._in_order(current_node.left_child):
                yield node
        yield current_node.key, current_node.val
        if current_node.right_child is not None:
            for node in self._in_order(current_node.right_child):
                yield node

    def reverse_order(self):
        if self.root is None:
            return [None]
        current_node = self.root
        return self._reverse_order(current_node)

    def _reverse_order(self, current_node):
        if current_node.right_child is not None:
            for node in self._reverse_order(current_node.right_child):
                yield node
        yield current_node.key, current_node.val
        if current_node.left_child is not None:
            for node in self._reverse_order(current_node.left_child):
                yield node

    def pre_order(self):
        if self.root is None:
            return [None]
        current_node = self.root
        return self._pre_order(current_node)

    def _pre_order(self, current_node):
        yield current_node.key, current_node.val
        if current_node.left_child is not None:
            for node in self._pre_order(current_node.left_child):
                yield node
        if current_node.right_child is not None:
            for node in self._pre_order(current_node.right_child):
                yield node

    def post_order(self):
        if self.root is None:
            return [None]
        current_node = self.root
        return self._post_order(current_node)

    def _post_order(self, current_node):
        if current_node.left_child is not None:
            for node in self._post_order(current_node.left_child):
                yield node
        if current_node.right_child is not None:
            for node in self._post_order(current_node.right_child):
                yield node
        yield current_node.key, current_node.val

    def breadth_first(self):
        if self.root is None:
            return [None]
        current_node = self.root
        return self._breadth_first(current_node)

    # def _breadth_first(self, current_node):
    #     current_level = [current_node]
    #     while current_level:
    #         next_level = []
    #         for node in current_level:
    #             if node.left_child is not None:
    #                 next_level.append(node.left)
    #             if node.right_child is not None:
    #                 next_level.append(node.right)
    #             if node.key is not None:
    #                 yield node.key, node.val
    #         current_level = next_level

    def _breadth_first(self, current_node):
        current_level = Queue()
        current_level.put(current_node)
        while not current_level.empty():
            node = current_level.get()
            if node.left_child is not None:
                current_level.put(node.left_child)
            if node.right_child is not None:
                current_level.put(node.right_child)
            yield node.key, node.val


class AvlTree(TreeWithNodes):
    """docstring for AvlTree"""
    def __init__(self):
        super(AvlTree, self).__init__()

    def _put(self, key, val, current_node, new_node):
        if new_node.key < current_node.key:
            if current_node.left_child is None:
                (current_node.left_child,
                 new_node.parent) = (new_node,
                                     current_node)
                self.size += 1
                self.put_update_balance_factor(current_node.left_child)
            else:
                self._put(key, val, current_node.left_child, new_node)
        elif new_node.key > current_node.key:
            if current_node.right_child is None:
                (current_node.right_child,
                 new_node.parent) = (new_node,
                                     current_node)
                self.size += 1
                self.put_update_balance_factor(current_node.right_child)
            else:
                self._put(key, val, current_node.right_child, new_node)
        else:
            current_node.val = new_node.val

    def _rm_node(self, key, current_node):
        if key == current_node.key:
            rebalance_node = None
            if current_node.left_child is None and current_node.right_child is None:
                if current_node == self.root:
                    self.root = None
                else:
                    if current_node.parent.left_child == current_node:
                        current_node.parent.left_child = None
                        current_node.parent.balance_factor -= 1
                    else:
                        current_node.parent.right_child = None
                        current_node.parent.balance_factor += 1
                    rebalance_node = current_node.parent
            else:
                replacement_node = None
                if current_node.get_balance_factor() >= 0:
                    if current_node.left_child.right_child is None:
                        replacement_node = current_node.left_child
                        replacement_node.right_child = current_node.right_child
                        if replacement_node.right_child is not None:
                            replacement_node.right_child.parent = replacement_node
                        if current_node != self.root:
                            if current_node.parent.left_child == current_node:
                                current_node.parent.left_child = replacement_node
                            else:
                                current_node.parent.right_child = replacement_node
                        replacement_node.balance_factor = current_node.balance_factor - 1
                        rebalance_node = replacement_node
                    else:
                        replacement_node = self._grab_right(current_node.left_child)
                        replacement_node.parent.right_child = replacement_node.left_child
                        if replacement_node.left_child is not None:
                            replacement_node.left_child.parent = replacement_node.parent
                        replacement_node.left_child = current_node.left_child
                        if replacement_node.left_child is not None:
                            replacement_node.left_child.parent = replacement_node
                        replacement_node.right_child = current_node.right_child
                        if replacement_node.right_child is not None:
                            replacement_node.right_child.parent = replacement_node
                        if current_node != self.root:
                            if current_node.parent.left_child == current_node:
                                current_node.parent.left_child = replacement_node
                            else:
                                current_node.parent.right_child = replacement_node
                        replacement_node.balance_factor = current_node.balance_factor
                        rebalance_node = replacement_node.parent
                        rebalance_node.balance_factor += 1
                else:
                    if current_node.right_child.left_child is None:
                        replacement_node = current_node.right_child
                        replacement_node.left_child = current_node.left_child
                        if replacement_node.left_child is not None:
                            replacement_node.left_child.parent = replacement_node
                        if current_node != self.root:
                            if current_node.parent.left_child == current_node:
                                current_node.parent.left_child = replacement_node
                            else:
                                current_node.parent.right_child = replacement_node
                        replacement_node.balance_factor = current_node.balance_factor + 1
                        rebalance_node = replacement_node
                    else:
                        replacement_node = self._grab_left(current_node.right_child)
                        replacement_node.parent.left_child = replacement_node.right_child
                        if replacement_node.right_child is not None:
                            replacement_node.right_child.parent = replacement_node.parent
                        replacement_node.left_child = current_node.left_child
                        if replacement_node.left_child is not None:
                            replacement_node.left_child.parent = replacement_node
                        replacement_node.right_child = current_node.right_child
                        if replacement_node.right_child is not None:
                            replacement_node.right_child.parent = replacement_node
                        if current_node != self.root:
                            if current_node.parent.left_child == current_node:
                                current_node.parent.left_child = replacement_node
                            else:
                                current_node.parent.right_child = replacement_node
                        replacement_node.balance_factor = current_node.balance_factor
                        rebalance_node = replacement_node.parent
                        rebalance_node.balance_factor -= 1
                if current_node == self.root:
                    self.root = replacement_node
                    replacement_node.balance_factor = current_node.balance_factor
                else:
                    replacement_node.parent = current_node.parent
            if rebalance_node is not None:
                self.remove_update_balance_factor(rebalance_node)
            self.size -= 1

        elif key < current_node.key:
            if current_node.left_child is None:
                raise KeyError
            self._rm_node(key, current_node.left_child)
        else:
            if current_node.right_child is None:
                raise KeyError
            self._rm_node(key, current_node.right_child)


    def get_balance_factor(self, node):
        return node.balance_factor

    def put_update_balance_factor(self, update_node):
        if update_node.balance_factor > 1 or update_node.balance_factor < -1:
            self.rebalance_node(update_node)
            return
        if update_node.parent is not None:
            if update_node.parent.left_child == update_node:
                update_node.parent.balance_factor += 1
            elif update_node.parent.right_child == update_node:
                update_node.parent.balance_factor -= 1
            if update_node.parent.balance_factor != 0:
                self.put_update_balance_factor(update_node.parent)

    def remove_update_balance_factor(self, update_node):
        if update_node.balance_factor > 1 or update_node.balance_factor < -1:
            self.rebalance_node(update_node)
            return
        if update_node.parent is not None:
            if update_node.balance_factor == 0:
                if update_node.parent.left_child == update_node:
                    update_node.parent.balance_factor -= 1
                else:
                    update_node.parent.balance_factor += 1
                self.remove_update_balance_factor(update_node.parent)

    def rebalance_node(self, rebalance_node):
        if rebalance_node.balance_factor < 0:
            if rebalance_node.right_child.balance_factor > 0:
                self.rotate_right(rebalance_node.right_child)
            self.rotate_left(rebalance_node)
        if rebalance_node.balance_factor > 0:
            if rebalance_node.left_child.balance_factor < 0:
                self.rotate_left(rebalance_node.left_child)
            self.rotate_right(rebalance_node)

    def rotate_right(self, rot_node):
        new_root = rot_node.left_child
        rot_node.left_child = new_root.right_child
        if new_root.right_child is not None:
            new_root.right_child.parent = rot_node
        new_root.parent = rot_node.parent
        if rot_node == self.root:
            self.root = new_root
        else:
            if rot_node.parent.left_child == rot_node:
                rot_node.parent.left_child = new_root
            else:
                rot_node.parent.right_child = new_root
        new_root.right_child = rot_node
        rot_node.parent = new_root
        rot_node.balance_factor = (rot_node.balance_factor
                                   - 1 - max(new_root.balance_factor, 0))
        new_root.balance_factor = (new_root.balance_factor
                                   - 1 + min(rot_node.balance_factor, 0))

    def rotate_left(self, rot_node):
        new_root = rot_node.right_child
        rot_node.right_child = new_root.left_child
        if new_root.left_child is not None:
            new_root.left_child.parent = rot_node
        new_root.parent = rot_node.parent
        if rot_node == self.root:
            self.root = new_root
        else:
            if rot_node.parent.left_child == rot_node:
                rot_node.parent.left_child = new_root
            else:
                rot_node.parent.right_child = new_root
        new_root.left_child = rot_node
        rot_node.parent = new_root
        rot_node.balance_factor = (rot_node.balance_factor
                                   + 1 - min(new_root.balance_factor, 0))
        new_root.balance_factor = (new_root.balance_factor
                                   + 1 + max(rot_node.balance_factor, 0))


class BSTreeWithList(object):
    def __init__(self):
        self.btree_list = [0, None]
        self.size = 1

    def insert(self, key, val, index=1):
        if self.btree_list[index] is None or self.btree_list[index][0] == key:
            self.btree_list[index] = key, val
            while self.size < 2 * index + 1:
                self.btree_list.append(None)
                self.size += 1
        elif self.btree_list[index][0] > key:
            if self.size < 2 * index:
                self.btree_list[self.size] = key, val
            else:
                self.insert(key, val, 2 * index)

        elif self.btree_list[index][0] < key:
                if self.size < 2 * index + 1:
                    self.btree_list[self.size] = key, val
                else:
                    self.insert(key, val, 2 * index + 1)

    def __setitem__(self, key, val):
        return self.insert(key, val)

    def remove_node(self, key, index=1):
        if self.btree_list[index] is None:
            raise KeyError
        if key < self.btree_list[index][0]:
            self.remove_node(key, 2 * index)
        elif key > self.btree_list[index][0]:
            self.remove_node(key, 2 * index + 1)
        else:
            if self.btree_list[index * 2] is not None:
                self.btree_list[index] = self.grab_right(index * 2)
            elif self.btree_list[index * 2 + 1] is not None:
                self.btree_list[index] = self.grab_left(index * 2 + 1)
            else:
                self.btree_list[index] = None
        while self.btree_list[self.size // 2] is None:
            self.btree_list.pop()
            self.size -= 1

    def __delitem__(self, key):
        return self.remove_node(key)

    def grab_right(self, index):
        if self.btree_list[2 * index] is None:
            new_node = self.btree_list[index]
            self.btree_list[index] = self.btree_list[2 * index + 1]
            return new_node
        else:
            return self.grab_right(index)

    def grab_left(self, index):
        if self.grab_right[2 * index + 1] is None:
            new_node = self.btree_list[index]
            self.btree_list[index] = self.btree_list[2* index]
            return new_node
        else:
            return self.grab_left(index)

    def contains(self, key, index=1):
        if self.btree_list[index] is None:
            return False
        elif key < self.btree_list[index][0]:
            return self.contains(key, 2 * index)
        elif key > self.btree_list[index][0]:
            return self.contains(key, 2 * index + 1)
        else:
            return True

    def __contains__(self, key):
        return self.contains(key)

    def return_val(self, key, index=1):
        if self.btree_list[index] is None:
            raise KeyError
        elif key < self.btree_list[index][0]:
            return self.return_val(key, 2 * index)
        elif key > self.btree_list[index][0]:
            return self.return_val(key, 2 * index + 1)
        else:
            return self.btree_list[index][1]

    def __getitem__(self, key):
        return self.return_val(key)

    def height(self, index=1):
        if self.btree_list[2 * index] is None and self.btree_list[2 * index + 1] is None:
            return 0
        elif self.btree_list[2 * index] is None:
            return self.height(2 * index + 1) + 1
        elif self.btree_list[2 * index + 1] is None:
            return self.height(2 * index) + 1
        else:
            return max(self.height(2 * index + 1), self.height(2 * index)) + 1

    def breadth_first(self):
        for node in self.btree_list:
            if node is not None and node != 0:
                yield node

    def in_order(self, index=1):
        if self.btree_list[2 * index] is not None:
            for node in self.in_order(2 * index):
                yield node
        yield self.btree_list[index]
        if self.btree_list[2 * index + 1] is not None:
            for node in self.in_order(2 * index + 1):
                yield node

    def pre_order(self, index=1):
        yield self.btree_list[index]
        if self.btree_list[2 * index] is not None:
            for node in self.in_order(2 * index):
                yield node
        if self.btree_list[2 * index + 1] is not None:
            for node in self.in_order(2 * index + 1):
                yield node
    def post_order(self, index=1):
        if self.btree_list[2 * index] is not None:
            for node in self.in_order(2 * index):
                yield node
        if self.btree_list[2 * index + 1] is not None:
            for node in self.in_order(2 * index + 1):
                yield node
        yield self.btree_list[index]

if __name__ == '__main__':
    tree = TreeWithNodes()
    # tree = AvlTree()
    tree[20] = 'orange'
    tree[30] = 'white'
    tree[10] = 'yellow'
    tree[15] = 'blue'
    tree[5] = 'gold'
    tree[6] = 'brown'
    print list(tree.in_order())
    print list(tree.reverse_order())
