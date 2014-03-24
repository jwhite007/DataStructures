#! /usr/bin/env python

import unittest
from data_structures import stack


class TestStack(unittest.TestCase):

    def testPushToEmpty(self):
        self.my_stack = stack.Stack()
        self.my_stack.push(5)
        self.assertEqual(5, self.my_stack.top.val)

    def testPushToNonEmpty(self):
        self.my_stack = stack.Stack()
        self.my_stack.push(5)
        self.my_stack.push(4)
        self.assertEqual(4, self.my_stack.top.val)

    def testPopFromNonEmpty(self):
        self.my_stack = stack.Stack()
        self.my_stack.push(5)
        self.assertEqual(5, self.my_stack.pop())

    def testPopFromEmpty(self):
        self.my_stack = stack.Stack()
        self.failureException("Uh oh!!  You're trying to pop from an empty \
            stack", self.my_stack.pop())

if __name__ == "__main__":
    unittest.main()
