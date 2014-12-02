#! /usr/bin/env python


# from data_structures.stack import Stack
from stack import Stack
import timeit
from collections import defaultdict


class Peg(Stack):
    """docstring for Peg"""
    def __init__(self, prev=None, next=None):
        super(Peg, self).__init__()
        self.prev = prev
        self.next = next


def print_peg(peg):
    l = []
    if peg.top is not None:
        i = peg.top
        while i is not None:
            l.append(i.val)
            i = i.next
    return l


def move_over(rings):
    peg1 = Peg()
    peg2 = Peg()
    peg3 = Peg()
    peg1.next = peg2
    peg2.prev, peg2.next = peg1, peg3
    peg3.prev = peg2

    for i in range(rings, 0, -1):
        peg1.push(i)

    # print 'peg1 before: ' + str(print_peg(peg1))
    # print 'peg2 before: ' + str(print_peg(peg2))
    # print 'peg3 before: ' + str(print_peg(peg3))

    l = peg1.size()
    cpeg = peg1
    direction = 'right'
    # count = 0

    while peg3.size() < l:
        if direction == 'right':
            if cpeg.is_empty():
                cpeg = cpeg.next
                direction = 'left'
            elif cpeg.next is not None:
                if cpeg.next.is_empty() or cpeg.peek() < cpeg.next.peek():
                    cpeg.next.push(cpeg.pop())
                    cpeg = cpeg.next
                elif cpeg.peek() > cpeg.next.peek():
                    cpeg = cpeg.next
                    direction = 'left'
            else:
                cpeg = cpeg.prev
                direction = 'left'

        if direction == 'left':
            if cpeg.is_empty():
                cpeg = cpeg.prev
                direction = 'right'
            elif cpeg.prev is not None:
                if cpeg.prev.is_empty() or cpeg.peek() < cpeg.prev.peek():
                    cpeg.prev.push(cpeg.pop())
                    cpeg = cpeg.prev
                else:
                    cpeg = cpeg.prev
                    direction = 'right'
            else:
                cpeg = cpeg.next
                direction = 'right'

    # print 'peg1 after: ' + str(print_peg(peg1))
    # print 'peg2 after: ' + str(print_peg(peg2))
    # return 'peg3 after: ' + str(print_peg(peg3))
    return None


def move_tower(height, fromPole,  withPole, toPole):
    if height >= 1:
        print("\t"*(height - 1) + "moving tower of height: " + str(height) + " from " + str(fromPole) + " to " + str(toPole) + " with " + str(withPole))
        move_tower(height - 1, fromPole, toPole, withPole)
        move_disk(height, fromPole, toPole)
        move_tower(height - 1, toPole, withPole, fromPole)


def move_disk(height, fp, tp):
    print("\t"*(height - 1) + "moving disk from " + str(fp) + " to " + str(tp))
    if isinstance(tp, list):
        tp.append(fp.pop())


def time_move_tower(rings):
    stackA = list()
    stackB = list()
    stackC = list()
    stackA.append("A")
    for i in range(1, rings + 1):
        stackA.append(i)
    stackB.append("B")
    stackC.append("C")
    move_tower(rings, stackA, stackC, stackB)

if __name__ == '__main__':
    # move_tower(3,"fp","wp","tp")
    stackA = list()
    stackB = list()
    stackC = list()
    stackA.append("A")
    stackA.append(1)
    stackA.append(2)
    stackA.append(3)
    stackB.append("B")
    stackC.append("C")

    print stackA
    print stackB
    print stackC
    move_tower(len(stackA)-1, stackA, stackB, stackC)
    print stackA
    print stackB
    print stackC

    # move_tower(3, "A", "B", "C")

    # s = 'move_over(3)'
    # t = 'move_over(4)'
    # u = 'move_over(5)'
    # ts = timeit.timeit(stmt=s, setup='from __main__ import move_over', number=10)
    # tt = timeit.timeit(stmt=t, setup='from __main__ import move_over', number=10)
    # tu = timeit.timeit(stmt=u, setup='from __main__ import move_over', number=10)
    # # print tt/ts
    # # print tu/tt
    # print str(ts) + "\n" + str(tt) + "\n" + str(tu)
    #
    #
    # d1 = defaultdict(int)
    # d2 = defaultdict(int)
    # d3 = defaultdict(int)
    # for i in range(3, 11):
    #     d1[i] = timeit.timeit(stmt='move_over('+str(i)+')', setup='from __main__ import move_over', number=10)
    #     d2[i] = timeit.timeit(stmt='time_move_tower('+str(i)+')', setup='from __main__ import time_move_tower', number=10)
    # for key in d1:
    #     d3[key] = d1[key] / d2[key]
    # print d1
    # print d2
    # print d3

    # peg = Peg()
    # peg.push(1)
    # peg.push(2)
    # print peg.size()
    # print peg.is_empty()
    # print peg.pop()
    # peg.pop()
    # print peg.is_empty()

    # print move_over(5)
