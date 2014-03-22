#! /usr/bin/env python


def insort(l):
    for i in range(1, len(l)):
        focus, comp_index = l[i], i - 1
        while comp_index >= 0:
            if focus < l[comp_index]:
                l[i], l[comp_index] = l[comp_index], focus
                i -= 1
                comp_index -= 1
            else:
                break


if __name__ == '__main__':

    l = [8, 4, 5, 6, 2, 1]
    (insort(l))
    print(l)
