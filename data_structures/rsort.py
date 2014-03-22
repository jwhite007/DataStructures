#! /usr/bin/env python


def rsort(l, radix):

    place, breakout = 1, False

    while breakout is False:

        count = 0
        buckets = [list() for i in range(radix)]

        for i in l:

            floor = i / place

            if floor == 0:

                count += 1

            buckets[floor % radix].append(i)

        l = []

        for bucket in buckets:

            l += bucket

        place *= radix

        if len(buckets[0]) == count:

            breakout = True

    return l




if __name__ == '__main__':
    l = [8, 502, 401, 5, 20, 3, 400, 7, 1001, 15, 25, 30, 2, 4]
    print(rsort(l, 10))

