#! /usr/bin/env python


class Node(object):

    def __init__(self, val):

        self.val = val
        self.next = None

    def __str__():
        pass


class Linkedlist(object):

    def __init__(self):

        self.head = None

    def insert(self, val):

        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next, self.head = self.head, new_node

    def pop(self):

        if self.head is not None:
            popped, self.head = self.head.val, self.head.next
            return popped
        else:
            return None

    def size(self):

        i = self.head
        counter = 0
        while i is not None:
            i = i.next
            counter += 1
        return counter

    def search(self, val):

        i = self.head
        while i is not None:
            if i.val == val:
                return val
            else:
                i = i.next
        else:
            return None

    def remove(self, val):

        i = self.head
        if i.val == val:
            self.pop()
        else:
            if self.head is not None:
                while i.next is not None:
                    if i.next.val == val:
                        i.next = i.next.next
                        break
                    i = i.next

    def print_me(self):
        i = self.head
        linked_list = []
        while i is not None:
            linked_list.append(i.val)
            i = i.next
        return str(linked_list)

    def print_kth_from_nth(self, k, n):
        i = self.head
        o = n
        p = self.head
        while o > 1:
            p = p.next
            o -= 1
        while True:
            l = k
            c = i
            while l > 0:
                c = c.next
                l -= 1
            if c is p:
                return i.val
            i = i.next
