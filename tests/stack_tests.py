#! /usr/bin/env python

import unittest
from data_structures.stack import Stack


class TestStack(unittest.TestCase):

    def test_push_to_empty(self):
        self.my_stack = Stack()
        self.my_stack.push(5)
        self.assertEqual(5, self.my_stack.top.val)

    def test_push_to_non_empty(self):
        self.my_stack = Stack()
        self.my_stack.push(5)
        self.my_stack.push(4)
        self.assertEqual(4, self.my_stack.top.val)

    def test_pop_from_non_empty(self):
        self.my_stack = Stack()
        self.my_stack.push(5)
        self.assertEqual(5, self.my_stack.pop())

    def test_pop_from_empty(self):
        self.my_stack = Stack()
        self.failureException("Uh oh!!  You're trying to pop from an empty \
            stack", self.my_stack.pop())

if __name__ == "__main__":
    unittest.main()
