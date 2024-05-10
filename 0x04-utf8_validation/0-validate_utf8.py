#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    RemainingBytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if RemainingBytes == 0:
            while mask & byte:
                RemainingBytes += 1
                mask = mask >> 1

            if RemainingBytes == 0:
                continue

            if RemainingBytes == 1 or RemainingBytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
        RemainingBytes -= 1

    return RemainingBytes == 0
