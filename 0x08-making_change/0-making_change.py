#!/usr/bin/python3
"""Making Change."""


def makeChange(coins, total):
    """Given a list of coins and a total, return the fewest"""
    if total <= 0:
        return 0

    sub_total = 0
    counter = 0
    while sub_total < total:
        sorted_list = sorted(coins, reverse=True)
        for c in sorted_list:
            while (sub_total + c) <= total:
                sub_total = sub_total + c
                counter += 1

        if sub_total != total:
            return -1
        else:
            return counter
