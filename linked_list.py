#! /usr/bin/env python


class Node(object):

    def __init__(self, val):

        self.val = val
        self.next = None


class Linkedlist(object):

    def __init__(self):

        self.head = None

    def insert(self, val):

        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):

        if self.head is not None:
            popped = self.head.val
            self.head = self.head.next
            print(popped)
        else:
            return "empty linked list"

    def size(self):

        if self.head is not None:
            i = self.head
            counter = 0
            while i is not None:
                i = i.next
                counter += 1
            return counter
        else:
            return 0

    def search(self, val):

        if self.head is not None:
            i = self.head
            while i is not None:
                if i.val == val:
                    return val
                else:
                    i = i.next
            else:
                return None
        else:
            return None

    def remove(self, val):

        if self.head is not None:
            i = self.head
            while i is not None:
                if i.next.val == val:
                    i.next = i.next.next
                    i.next.next = None
                    # i = i.next
                break

    def print_me(self):
        i = self.head
        linked_list = []
        while i is not None:
            linked_list.append(i.val)
            i = i.next
        return linked_list

if __name__ == '__main__':
    """Documentaion and tests"""

    linky = Linkedlist()
    linky.insert(1)
    linky.insert(2)
    linky.insert(3)
    linky.insert(4)
    print(linky.print_me())
    print(linky.size())
    linky.pop()
    print(linky.print_me())
    print(linky.size())
    print(linky.search(3))
    print(linky.search(4))
    linky.remove(2)
    print(linky.print_me())
