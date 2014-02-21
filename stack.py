#! /usr/bin/env python


class Node(object):

    def __init__(self, val):

        self.val = val
        self.next = None

    def __str__():
        pass


class Stack(object):

    def __init__(self):

        self.top = None

    def __str__():
        pass

    def push(self, val):

        new_node = Node(val)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next, self.top = self.top, new_node

    def pop(self):
        try:
            popped, self.top = self.top.val, self.top.next
            return popped
        except AttributeError:
            print("Uh oh!!  You're trying to pop from an empty stack")
