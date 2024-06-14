#!/usr/bin/python3
"""Prime Game"""


def isPrime(n):
    """
    Checks if n is prime
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxDivisor = int(n**0.5) + 1
    for d in range(3, maxDivisor, 2):
        if n % d == 0:
            return False
    return True


def isMultiple(m, n):
    """
    Checks if m is multiple of n
    """
    return m % n == 0


def toggle(value):
    """
    Toggles between 0 and 1
    """
    return 1 - value


def isWinner(x, nums):
    """
    isWinner Function: x and n will not be larger than 10,000
    * Maria Always plays first
    * Ben is the other player
    * Each player plays optimally meaning they choose the best choice
    """
    players = ("Maria", "Ben")
    turn = 0
    roundsWon = {"Maria": 0, "Ben": 0}
    chosen = []
    for round in range(x):
        for num in nums:
            for d in range(1, num+1):
                if not isPrime(d):
                    continue
                for m in chosen:
                    if isMultiple(m, d):
                        continue
                if d not in chosen:
                    chosen.append(d)
                turn = toggle(turn)
            chosen = []
        roundsWon[players[turn]] += 1

    if roundsWon["Maria"] > roundsWon["Ben"]:
        return "Maria"
    else:
        return "Ben"
