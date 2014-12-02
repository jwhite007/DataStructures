#! /usr/bin/env python

import bsort, insort, msort, qsort, rsort, selection_sort, ssort

list_list = [[5, 4, 3, 2, 1],
             [30, 28, 27, 26, 25, 24, 23, 22, 21]
             ]


if __name__ == '__main__':
    from timeit import timeit
    from random import randrange
    # for l in list_list:
    # print l
    l = [randrange(1, 10001) for i in range(10001)]
    # l = range(10000, 0, -1)
    print("bubbleSort:".ljust(20) +
          str(timeit(stmt="bsort.bubble_sort(l)",
                     setup="from __main__ import bsort, l",
                     number=10)))
    print("shortBubbleSort:".ljust(20) +
          str(timeit(stmt="bsort.short_bubble_sort(l)",
                     setup="from __main__ import bsort, l",
                     number=10)))
    print("insort:".ljust(20) +
          str(timeit(stmt="insort.insort(l)",
                     setup="from __main__ import insort, l",
                     number=10)))
    print("msort:".ljust(20) +
          str(timeit(stmt="msort.msort(l)",
                     setup="from __main__ import msort, l",
                     number=10)))
    print("qsort:".ljust(20) +
          str(timeit(stmt="qsort.qsort(l)",
                     setup="from __main__ import qsort, l",
                     number=10)))
    print("rsort:".ljust(20) +
          str(timeit(stmt="rsort.rsort(l, 10)",
                     setup="from __main__ import rsort, l",
                     number=10)))
    print("selectionSort:".ljust(20) +
          str(timeit(stmt="selection_sort.selection_sort(l)",
                     setup="from __main__ import selection_sort, l",
                     number=10)))
    print("shellSort:".ljust(20) +
          str(timeit(stmt="ssort.shell_sort(l)",
                     setup="from __main__ import ssort, l",
                     number=10)))
