#! /usr/bin/env python

from stack import Stack


class Node(object):

    def __init__(self, val):

        self.val = val
        self.next = None
        self.prev = None


class Queue(object):

    def __init__(self):

        self.head = None
        self.tail = None
        self.__size = 0

    def enqueue(self, val):

        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.__size += 1
        else:
            self.tail.next, new_node.prev, self.tail = new_node, self.tail, new_node
            self.__size += 1

    def dequeue(self):

        try:
            dequeued, self.head = self.head.val, self.head.next
            self.__size -= 1
            return dequeued
        except AttributeError:
            return 'Uh oh!!  Queue is empty'

    def get_size(self):
        return self.__size

    def is_empty(self):
        if self.__size == 0:
            return True
        else:
            return False


class TwoStackQueue(object):

    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, val):
        if self.dequeue_stack.size() != 0:
            while self.dequeue_stack.size() != 0:
                self.enqueue_stack.push(self.dequeue_stack.pop())
        self.enqueue_stack.push(val)

    def dequeue(self):
        if self.dequeue_stack.size() == 0:
            if self.enqueue_stack.size() == 0:
                msg = 'Queue is empty'
                raise Warning(msg)
            else:
                while self.enqueue_stack.size() > 1:
                    self.dequeue_stack.push(self.enqueue_stack.pop())
                return self.enqueue_stack.pop()
        else:
            return self.dequeue_stack.pop()

    def size(self):
        if self.enqueue_stack.size() == 0:
            return self.dequeue_stack.size()
        else:
            return self.enqueue_stack.size()

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    myQueue = TwoStackQueue()
    print myQueue.is_empty()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    myQueue.enqueue(4)
    myQueue.enqueue(5)
    print myQueue.is_empty()
    print myQueue.size()
    print myQueue.dequeue()
    print myQueue.size()
