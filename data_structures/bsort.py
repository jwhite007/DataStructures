#! /usr/bin/env python


def bubble_sort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def short_bubble_sort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i+1], alist[i]
        passnum = passnum-1
    # return alist

if __name__ == '__main__':
    import timeit
    from random import randrange
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    short_bubble_sort(alist)
    print alist
    # alist = [30, 28, 27, 26, 25, 24, 23, 22, 21]
    # ls = []
    # for i in range(10001):
    #     ls.append(randrange(1, 10001))
    # print timeit.timeit(stmt="bubble_sort(alist)",
    #                     setup="from __main__ import bubbleSort, alist",
    #                     number=10)
    # print timeit.timeit(stmt="short_bubble_sort(alist)",
    #                     setup="from __main__ import shortBubbleSort, alist",
    #                     number=10)
