#! /usr/bin/env python


def insort(alist):
    if not isinstance(alist, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)
    else:
        if len(alist) < 1:
            msg = "Can't sort an empty list"
            raise ValueError(msg)
        elif len(alist) == 1:
            return alist
        else:
            for i in range(1, len(alist)):
                focus, comp_index = alist[i], i - 1
                while comp_index >= 0:
                    if focus < alist[comp_index]:
                        alist[i] = alist[comp_index]
                        i -= 1
                        comp_index -= 1
                    else:
                        break
                alist[i] = focus
        # else:
        #     for i in range(1, len(alist)):
        #         focus, pos = alist[i], i
        #         while pos > 0 and focus < alist[pos - 1]:


def insort2(alist):
    if not isinstance(alist, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)
    else:
        if len(alist) < 1:
            msg = "Can't sort an empty list"
            raise ValueError(msg)
        elif len(alist) == 1:
            return alist
        else:
            for i in range(1, len(alist)):
                focus, pos = alist[i], i
                while pos > 0 and alist[pos - 1] > focus:
                    alist[pos] = alist[pos - 1]
                    pos -= 1
                alist[pos] = focus


def insort3(alist):
    if not isinstance(alist, list):
        msg = "This method only works on lists.  Please input a list."
        raise ValueError(msg)
    else:
        if len(alist) < 1:
            msg = "Can't sort an empty list"
            raise ValueError(msg)
        elif len(alist) == 1:
            return alist
        else:
            for i in range(1, len(alist)):
                focus, comp_index = alist[i], i - 1
                while comp_index >= 0:
                    if focus < alist[comp_index]:
                        alist[i], alist[comp_index] = alist[comp_index], focus
                        i -= 1
                        comp_index -= 1


if __name__ == '__main__':
    # import timeit
    # from random import randrange
    ls = [5, 4, 3, 2, 1]
    insort(ls)
    print ls
    # l = []
    # for i in range(10001):
    #     l.append(randrange(1, 10001))

    # print timeit.timeit(stmt="insort(l)",
    #                     setup="from __main__ import insort, l",
    #                     number=100)
    # print timeit.timeit(stmt="insort2(l)",
    #                     setup="from __main__ import insort2, l",
    #                     number=100)
    # print timeit.timeit(stmt="insort3(l)",
    #                     setup="from __main__ import insort3, l",
    #                     number=10)
