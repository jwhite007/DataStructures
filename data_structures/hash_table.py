#! /usr/bin/env python


class HashTable(object):
    """docstring for HashTable"""
    def __init__(self, size):

        self.head = None
        self.size = size
        for i in range(self.size):
            new_index = Index(i)
            if self.head is None:
                self.head = new_index
            else:
                new_index.next, self.head = self.head, new_index

    def set(self, key, val):

        if isinstance(key, str):
            index = self.hash(key) % self.size
            i = self.head
            while i is not None:
                if i.val == index:
                    if i.child is None:
                        i.child = Child((key, val))
                    else:
                        c = i.child
                        while c is not None:
                            if c.val[0] == key:
                                return 'key already in use'
                            else:
                                c = c.next
                        else:
                            new_child = Child((key, val))
                            new_child.next, i.child = i.child, new_child
                else:
                    i = i.next
        else:
            return 'key must be a string!'

    def get(self, key):

        if isinstance(key, str):
            index = self.hash(key) % self.size
            i = self.head
            while i is not None:
                if i.val == index:
                    c = i.child
                    while c is not None:
                        if c.val[0] == key:
                            return c.val[1]
                        else:
                            c = c.next
                    else:
                        return 'key is not in table'
                else:
                    i = i.next
            else:
                return None
        else:
            return 'key must be a string!'

    def hash(self, key):
        total_ord = 0
        for i in key:
            total_ord = total_ord + ord(i)
        return total_ord


class Index(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.child = None


class Child(object):

    def __init__(self, val):
        self.val = val
        self.next = None
