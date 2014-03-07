#! /usr/bin/env python

from calendar import monthrange
import hash_table


def make_month(year, month):
    first_day, total_days = monthrange(year, month)
    ht = hash_table.HashTable(10)
    ht.set('0', 'Mo')
    ht.set('1', 'Tu')
    ht.set('2', 'We')
    ht.set('3', 'Th')
    ht.set('4', 'Fr')
    ht.set('5', 'Sa')
    ht.set('6', 'Su')

    def method(num):
        if num <= total_days:
            key = (num - 1 + first_day) % 7
            return ht.get(str(key))
        else:
            msg = "Day is larger than days in month"
            raise ValueError(msg)
    return method
