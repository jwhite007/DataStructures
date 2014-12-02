#! /usr/bin/env python


class ListIterator(object):
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def next(self):
        if self.current is None:
            raise StopIteration

        val = self.current.val
        self.current = self.current.next
        return val

class Node(object):

    def __init__(self, val):

        self.val = val
        self.next = None

    def __str__():
        pass


class LinkedList(object):

    def __init__(self):

        self.head = None
        self.index = self.head

    def __iter__(self):
        return ListIterator(self.head)
    # def __iter__(self):
    #     return self

    # def next(self):
    #     if self.index is None:
    #         raise StopIteration
    #     val = self.index.val
    #     self.index = self.index.next
    #     return val

    def _get(self, index):
        count = 0
        current_node = self.head
        while count != index:
            current_node = current_node.next
            if current_node is None:
                return 'index out of range'
            count += 1
        return current_node.val

    def __getitem__(self, index):
        return self._get(index)

    def _set(self, index, val):
        count = 0
        current_node = self.head
        while count != index:
            current_node = current_node.next
            if current_node is None:
                return 'index out of range'
            count += 1
        current_node.val = val

    def __setitem__(self, index, val):
        return self._set(index, val)

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
                return True
            else:
                i = i.next
        return False

    def remove(self, val):

        i = self.head
        if i.val == val:
            self.head = self.head.next
        else:
            if self.head is not None:
                while i.next is not None:
                    if i.next.val == val:
                        i.next = i.next.next
                        break
                    i = i.next

    def remove_index(self, index):
        count = 0
        current_node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            while count != index - 1:
                current_node = current_node.next
                count += 1
            current_node.next = current_node.next.next

    def __delitem__(self, index):
        return self.remove_index(index)

    def print_me(self):
        i = self.head
        linked_list = []
        while i is not None:
            linked_list.append(i.val)
            i = i.next
        return linked_list

    # def return_kth_from_nth(self, k, n):
    #     nth = self.head
    #     for _ in range(n - 1):
    #         nth = nth.next
    #     kth = self.head
    #     while True:
    #         end = kth
    #         for _ in range(k):
    #             end = end.next
    #         if end is nth:
    #             return kth.val
    #         kth = kth.next

    def return_kth_from_nth(self, k, n):
        diff = n - k
        kth = self.head
        for _ in range(diff - 1):
            kth = kth.next
        return kth.val

    def rem_dups(self):
        i = self.head
        k = i.next
        while i.next is not None:
            while k is not None:
                if i.val == k.val:
                    self.remove(k.val)
                k = k.next
            i = i.next
            k = i.next

    def partition_around_x(self, x):
        i = self.head
        while i.next is not None:
            if i.next.val == x:
                i.next = i.next.next
                self.insert(x)
            i = i.next
        i = self.head
        while i.next is not None:
            if i.next.val < x:
                val = i.next.val
                i.next = i.next.next
                self.insert(val)
            else:
                i = i.next

    def is_palindrome(self):
        i = self.head
        k = i
        j = None
        while i is not j:
            while k.next is not j:
                k = k.next
            if i.val != k.val:
                return False
            else:
                i = i.next
                j = k
                k = i
            if j.next is i:
                break
        return True

    def reverse(self):
        # import pdb; pdb.set_trace()
        i = self.head
        count = self.size() - 1
        while count > 0:
            val = i.next.val
            i.next = i.next.next
            self.insert(val)
            count -= 1


def sum_numbers_as_linked_lists_head(ll1, ll2):
    # ones place is in head position
    i = ll1.head
    k = ll2.head
    sumll = LinkedList()
    s = 0
    rem = 0
    idone = False
    kdone = False
    breakout = False
    while breakout is False:
        if idone is True:
            ival = 0
        if kdone is True:
            kval = 0
        if i.next is None:
            ival = i.val
            idone = True
        else:
            ival = i.val
            i = i.next
        if k.next is None:
            kval = k.val
            kdone = True
        else:
            kval = k.val
            k = k.next
        total = ival + kval + rem
        if total > 9:
            total = total % 10
            rem = 1
            if s == 0:
                sumll.insert(total)
                s = sumll.head
            else:
                new_node = Node(total)
                s.next = new_node
                s = s.next
        else:
            rem = 0
            if s == 0:
                sumll.insert(total)
                s = sumll.head
            else:
                new_node = Node(total)
                s.next = new_node
                s = s.next
            new_node = Node(total)
        if kdone is True and idone is True:
            if rem == 1:
                new_node = Node(rem)
                s.next = new_node
            breakout = True

    return sumll.print_me()


def sum_numbers_as_linked_lists_tail(ll1, ll2):
    # ones place is in tail position
    i = ll1.head
    j = None
    k = ll2.head
    l = None
    sumll = LinkedList()
    rem = 0
    ival = 0
    kval = 0
    idone = False
    kdone = False
    breakout = False

    while breakout is False:
        # import pdb; pdb.set_trace()
        if idone is True and kdone is False:
            ival = 0
            if k.next is l:
                kdone = True
            while k.next is not l:
                k = k.next
            kval = k.val
            l = k
            k = ll2.head
        if kdone is True and idone is False:
            kval = 0
            if i.next is j:
                idone = True
            while i.next is not j:
                i = i.next
            ival = i.val
            j = i
            i = ll1.head
        if idone is False and kdone is False:
            if ll1.head.next is j:
                idone = True
            if ll2.head.next is l:
                kdone = True
            while k.next is not l:
                k = k.next
            kval = k.val
            l = k
            k = ll2.head
            while i.next is not j:
                i = i.next
            ival = i.val
            j = i
            i = ll1.head

        total = ival + kval + rem
        if total > 9:
            total = total % 10
            rem = 1
            sumll.insert(total)
        else:
            rem = 0
            sumll.insert(total)
        if idone is True and kdone is True:
            if rem == 1:
                sumll.insert(rem)
            breakout = True
    return sumll.print_me()


class DLNode(Node):
    """docstring for DLNode"""
    def __init__(self, val):
        # super(DLNode, self).__init__()
        Node.__init__(self, val)
        self.prev = None


class DLinkedList(object):
    # Implemantation of a doubly-linked list
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = DLNode(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next, self.head.prev, self.head = \
                self.head, new_node, new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.val
            self.head, self.head.prev = self.head.next, None
            return popped

    def size(self):
        if self.head is None:
            return None
        else:
            i = self.head
            count = 1
            while i.next is not None:
                count += 1
                i = i.next
            return count

    def search(self, val):
        i = self.head
        while i is not None:
            if i.val == val:
                return True
            i = i.next
        return False

    def remove(self, val):

        i = self.head
        while i is not None:
            if i.val == val:
                if i is self.head:
                    self.head, self.head.prev = self.head.next, None
                    break
                if i.next is None:
                    i.prev.next = None
                else:
                    i.prev.next, i.next.prev = i.next, i.prev
                    break
            i = i.next

    def print_me(self):
        i = self.head
        l = []
        while i is not None:
            l.append(i.val)
            i = i.next
        return l


class CLinkedList(object):
    """docstring for CLinkedList"""
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            new_node = Node(val)
            self.head = new_node
            self.head.next = self.head
        else:
            new_node = Node(val)
            i = self.head
            while i.next is not self.head:
                i = i.next
            i.next, new_node.next, self.head = new_node, self.head, new_node

    def circ_value(self):
        i = self.head
        j = self.head
        breakout = False
        while breakout is False:
            i = i.next
            j = j.next.next
            if i is j:
                breakout = True
        return i.val

    def remove(self, val):
        i = self.head
        breakout = False
        while breakout is False:
            if i.next.val == val:
                if i.next is self.head:
                    i.next, self.head = i.next.next, i.next.next
                    breakout = True
                else:
                    i.next = i.next.next
                    breakout = True
            i = i.next

    def print_me(self):
        i = self.head
        cll = []
        breakout = False
        while breakout is False:
            cll.append(i.val)
            i = i.next
            if i is self.head:
                breakout = True
        return cll


if __name__ == '__main__':
    linky = LinkedList()
    linky.insert(1)
    linky.insert(2)
    linky.insert(3)
    linky.insert(4)
    linky.insert(5)
    print linky.return_kth_from_nth(0, 5)
    # print linky.return_kth_from_nth_2(1, 5)
