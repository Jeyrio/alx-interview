#!/usr/bin/python3
""" making changes """


def makeChange(coins, total):
    """ return the minimal change """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_change = 0
    sum_change = 0

    for a in coins:
        while sum_change < total:
            sum_change += a
            num_change += 1
        if sum_change == total:
            return num_change
        sum_change -= a
        num_change -= 1
    return -1
