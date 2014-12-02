#! /usr/bin/env python
from linked_list import LinkedList


class Index(LinkedList):
    """docstring for Index"""
    def __init__(self):
        super(Index, self).__init__()
        self.next = None
        self.val = None


class HashTable(object):
    """docstring for HashTable"""
    def __init__(self, size):
        super(HashTable, self).__init__()
        self.size = size
        self.head = None
        for i in range(self.size):
            new_index = Index()
            new_index.val = i
            if self.head is None:
                self.head = new_index
            else:
                new_index.next, self.head = self.head, new_index

    def set(self, key, val):
        try:
            hash = self.__hash(key) % self.size
        except TypeError:
            raise ValueError('key needs to be a string')
        bucket = self.head
        while hash != bucket.val:
            bucket = bucket.next
        bucket.insert((key, val))

    def get(self, key):
        try:
            hash = self.__hash(key) % self.size
        except TypeError:
            raise ValueError('key needs to be a string')
        bucket = self.head
        while hash != bucket.val:
            bucket = bucket.next
        node = bucket.head
        while key != node.val[0]:
            node = node.next
        return node.val[1]

    def __getitem__(self, key):
        return self.get(key)

    def __hash(self, key):
        sum_ords = 0
        for i in key:
            sum_ords += ord(i)
        return sum_ords


if __name__ == '__main__':
    hasher = HashTable(10)
    hasher.set('bill', 2)
    print hasher.get('bill')
    hasher.set('lilb', 1)
    print hasher.get('lilb')
    print hasher['bill']