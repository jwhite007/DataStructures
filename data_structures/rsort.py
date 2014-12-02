#! /usr/bin/env python


def rsort(alist, radix):
    if not isinstance(alist, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)

    else:
        place = 1

        while True:
            count = 0
            buckets = [list() for i in range(radix)]
            negbuckets = [list() for i in range(radix)]
            for i in alist:
                if i < 0:
                    floor = -i // place
                    negbuckets[floor % radix].append(i)
                    if floor == 0:
                        count += 1
                else:
                    floor = i // place
                    buckets[floor % radix].append(i)
                    if floor == 0:
                        count += 1

            alist = []

            for bucket in negbuckets[::-1]:
                alist += bucket

            for bucket in buckets:
                alist += bucket

            if len(buckets[0]) + len(negbuckets[0]) == count:
                break

            place *= radix

        return alist

def rsort_rec(alist, radix, place = 1):
    if not isinstance(alist, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)

    else:
        count = 0
        buckets = [list() for i in range(radix)]
        negbuckets = [list() for i in range(radix)]
        for i in alist:
            if i < 0:
                floor = -i // place
                negbuckets[floor % radix].append(i)
                if floor == 0:
                    count += 1
            else:
                floor = i // place
                buckets[floor % radix].append(i)
                if floor == 0:
                    count += 1

        alist = []

        for bucket in negbuckets[::-1]:
            alist += bucket

        for bucket in buckets:
            alist += bucket

        if len(buckets[0]) + len(negbuckets[0]) == count:
            return alist

        else:
            place *= radix
            return rsort_rec(alist, radix, place)

if __name__ == '__main__':
    from timeit import timeit
    from random import randrange
    # ALIST = [1000, 100, -1001, -1002, 0, -100, 1011, 111]
    # print rsort2(ALIST, 10)
    ALIST = [randrange(-200, 200) for i in range(100)]
    print timeit(stmt='rsort([randrange(-200, 200) for i in range(100)], 10)', setup='from __main__ import rsort, randrange', number=10000)
    print timeit(stmt='rsort_rec([randrange(-200, 200) for i in range(100)], 10)', setup='from __main__ import rsort_rec, randrange', number=10000)