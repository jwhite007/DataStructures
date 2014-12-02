#! /usr/bin/env python


def qsort(l):
    if not isinstance(l, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)
    else:
        if len(l) <= 1:
            return l
        pivot = l[len(l)//2]
        # index = l.index(pivot)
        # del l[len(l)//2]
        pl = [pivot]
        low = []
        high = []
        for i in range(len(l)):
            if i == len(l)//2:
                continue
            elif pivot >= l[i]:
                low.append(l[i])
            else:
                high.append(l[i])
        # l.insert(index, pivot)
        return qsort(low) + pl + qsort(high)


def qsort_med_of_3(l):
    if not isinstance(l, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)
    else:
        if len(l) <= 1:
            # print "printing single: " + str(l)
            return l
        plist = [l[0], l[len(l)//2], l[-1]]
        plist.sort()
        pivot = plist[1]
        index = l.index(pivot)
        del l[l.index(pivot)]
        pl = [pivot]
        low = []
        high = []
        for i in range(len(l)):
            if pivot >= l[i]:
                low.append(l[i])
            else:
                high.append(l[i])
        # print "printing low: " + str(low)
        # print "printing pivot: " + str(pivot)
        # print "printing high: " + str(high)
        # print ""
        l.insert(index, pivot)
        return qsort_med_of_3(low) + pl + qsort_med_of_3(high)


def qsort2(alist):
    qsort_helper(alist, 0, len(alist) - 1)


def qsort_helper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)
        qsort_helper(alist, first, splitpoint - 1)
        qsort_helper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and \
                alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = \
                alist[rightmark], alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


def qsort3(l):
    if not isinstance(l, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)
    else:
        if len(l) <= 1:
            return l
        pivot = l[len(l)//2]
        del l[len(l)//2]
        pl = [pivot]
        low = []
        high = []
        for i in range(len(l)):
            if pivot >= l[i]:
                low.append(l[i])
            else:
                high.append(l[i])
        return qsort3(low) + pl + qsort3(high)


if __name__ == '__main__':
    from timeit import timeit
    from random import randrange
    # import sys
    # sys.setrecursionlimit(5000)
    # print sys.getrecursionlimit()
    # l = [8, 5, 20, 3, 7, 15, 25, 30, 2, 4]
    # print qsort(l)
    # l = [randrange(1, 1001) for i in range(0, 1000)]
    # print l
    # print(qsort(l) == qsort3(l))
    # print qsort3(l)
    # print l
    # print qsort_med_of_3(l)
    # l = range(20, 0, -1)
    # print l
    # print(qsort(l))
    # qsort2(l)
    # print l
    l = [randrange(1, 10001) for i in range(0, 10001)]
    print(timeit(stmt="qsort(l)",
                 setup="from __main__ import qsort, l",
                 number=1000))
    print(timeit(stmt="qsort3(l)",
                 setup="from __main__ import qsort3, l",
                 number=1000))
    print(timeit(stmt="qsort_med_of_3(l)",
                 setup="from __main__ import qsort_med_of_3, l",
                 number=1000))
    print(timeit(stmt="qsort2(l)",
                 setup="from __main__ import qsort2, l; \
                 import sys; sys.setrecursionlimit(8000)",
                 number=1000))
