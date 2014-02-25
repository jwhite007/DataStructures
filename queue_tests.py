#! /usr/bin/env python

import unittest
import queue


class testQueue(unittest.TestCase):

    def test_enqueue_empty(self):
        my_queue = queue.Queue()
        my_queue.enqueue('1')
        self.assertEqual('1', my_queue.head.val)

    def test_enqueue_not_empty(self):
        my_queue = queue.Queue()
        my_queue.enqueue('1')
        my_queue.enqueue('2')
        self.assertEqual(('2', '1'), (my_queue.head.val, my_queue.tail.val))

    def test_dequeue_empty(self):
        my_queue = queue.Queue()
        self.failureException('Uh oh!!  Queue is empty', my_queue.dequeue())

    def test_dequeue_not_empty(self):
        my_queue = queue.Queue()
        my_queue.enqueue('4')
        my_queue.enqueue('3')
        my_queue.enqueue('2')
        self.assertEqual('4', my_queue.dequeue())

    def test_size_empty(self):
        my_queue = queue.Queue()
        self.assertEqual(0, my_queue.get_size())

    def test_size_not_empty(self):
        my_queue = queue.Queue()
        my_queue.enqueue('4')
        my_queue.enqueue('3')
        my_queue.enqueue('2')
        self.assertEqual(3, my_queue.get_size())

if __name__ == '__main__':
    unittest.main()
