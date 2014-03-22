#! /usr/bin/env python


def qsort(l):
    if len(l) <= 1:
        return l

    pivot = l[len(l)/2]
    del l[len(l)/2]
    pl = [pivot]
    low = []
    high = []

    for i in range(len(l)):

        if pivot >= l[i]:
            low.append(l[i])
        else:
            high.append(l[i])

    return qsort(low) + pl + qsort(high)

if __name__ == '__main__':
    l = [8, 5, 20, 3, 7, 15, 25, 30, 2, 4]
    print(qsort(l))
