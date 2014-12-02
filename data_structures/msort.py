#! /usr/bin/env python


def msort(l):
    if not isinstance(l, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)
    else:
        if len(l) <= 1:
            return l
        left, right = l[:(len(l) / 2)], l[(len(l) / 2):]
        left = msort(left)
        right = msort(right)
        return merge(left, right)


def merge(left, right):

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    i, j, m = 0, 0, []

    while len(m) < len(left) + len(right):

        if left[i] < right[j]:
            m.append(left[i])
            i += 1
        else:
            m.append(right[j])
            j += 1
        if i == len(left):
            m.extend(right[j:])
        if j == len(right):
            m.extend(left[i:])

    return m

def msort_in_place(l):
    if len(l) <= 1:
        return l
    left, right = l[:len(l)/2], l[len(l)/2:]
    msort_in_place(left)
    msort_in_place(right)

    i, j, m = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l[m] = left[i]
            i += 1
        else:
            l[m] = right[j]
            j += 1
        m += 1

    while i < len(left):
        l[m] = left[i]
        i += 1
        m += 1

    while j < len(right):
        l[m] = right[j]
        j += 1
        m += 1


if __name__ == '__main__':
    # from timeit import timeit
    # from random import randrange
    l = [1.2, 1.1, 4.6, 4.3, 3, 7, 8, -1]
    # l = ['P', 'y', 'T', 'h', 'O', 'n']
    print msort(l)
    # print l
    # l = [randrange(1, 10001) for i in range(10001)]

    # print timeit(stmt="msort(l)",
    #              setup="from __main__ import msort, l",
    #              number=100)
    # print timeit(stmt="msort_in_place(l)",
    #              setup="from __main__ import msort_in_place, l",
    #              number=100)
