#! /usr/bin/env python


def msort(l):
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
        elif j == len(right):
            m.extend(left[i:])
            break

    return m

if __name__ == '__main__':
    l = [8, 5, 20, 3, 7, 15, 25, 30, 2, 4]
    print(msort(l))

