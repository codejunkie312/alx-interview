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


def countPrimes(n):
    """
    Counts the number of primes up to n
    """
    count = 0
    for i in range(2, n+1):
        if isPrime(i):
            count += 1
    return count


def isWinner(x, nums):
    """
    isWinner Function: x and n will not be larger than 10,000
    * Maria Always plays first
    * Ben is the other player
    * Each player plays optimally meaning they choose the best choice
    """
    if x <= 0:
        return None

    roundsWon = {"Maria": 0, "Ben": 0}

    for num in nums:
        primes_count = countPrimes(num)
        if primes_count % 2 == 0:
            roundsWon["Ben"] += 1
        else:
            roundsWon["Maria"] += 1

    if roundsWon["Maria"] > roundsWon["Ben"]:
        return "Maria"
    elif roundsWon["Ben"] > roundsWon["Maria"]:
        return "Ben"
    else:
        return None
