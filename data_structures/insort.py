#! /usr/bin/env python


def insort(l):
    if not isinstance(l, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)
    else:
        if len(l) <= 1:
            return l
            msg = "Can't sort an empty list"
            raise ValueError(msg)
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
    pass
