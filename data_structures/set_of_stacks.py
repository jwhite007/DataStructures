#! /usr/bin/env python

from stack import Stack


class StackExt(Stack):
    """docstring for Stack_ext"""
    def __init__(self, limit):
        super(StackExt, self).__init__()
        self.next = None
        self.bottom = None
        self.limit = limit


class SetOfStacks(object):
    """docstring for SetOfStacks"""
    def __init__(self, limit):
        self.head = None
        self.limit = limit

    def push(self, value):
        if self.head is None:
            new_stack = StackExt(self.limit)
            self.head = new_stack
            self.head.push(value)
        else:
            if self.head.size() == self.limit:
                new_stack = StackExt(self.limit)
                new_stack.next, self.head = self.head, new_stack
                self.head.push(value)
            else:
                self.head.push(value)

    def pop(self):
        popped = self.head.pop()
        if self.head.size() == 0:
            self.head = self.head.next
        return popped

    # def popAt(self, index):


if __name__ == '__main__':
    sos = SetOfStacks(2)
    sos.push(1)
    sos.push(2)
    sos.push(3)
    sos.push(4)
    sos.push(5)
    sos.push(6)
    sos.push(7)
    sos.push(8)
    print sos.pop()
    print sos.head.top.val
    # print sos.head.next.top.val
