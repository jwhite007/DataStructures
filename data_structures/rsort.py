#! /usr/bin/env python


def rsort(l, radix):
    if not isinstance(l, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)

    else:

        place, breakout = 1, False

        while breakout is False:

            count = 0
            buckets = [list() for i in range(radix)]

            for i in l:

                floor = i // place

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
    pass
