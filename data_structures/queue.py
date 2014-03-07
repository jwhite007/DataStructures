#! /usr/bin/env python


class Node(object):

    def __init__(self, val):

        self.val = val
        self.next = None
        self.prev = None


class Queue(object):

    def __init__(self):

        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, val):

        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self._size += 1
        else:
            new_node.next, self.head.prev, self.head = self.head, new_node, new_node
            self._size += 1

    def dequeue(self):

        try:
            dequeued, self.tail = self.tail.val, self.tail.prev
            self._size -= 1
            return dequeued
        except AttributeError:
            print('Uh oh!!  Queue is empty')

    def get_size(self):
        return self._size
