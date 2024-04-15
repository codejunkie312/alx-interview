#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Contains lists that have keys that unlock subsequent lists
    with first Array (at index 0) unlocked by default"""
    if type(boxes) is not list:
        print("These are not boxes.")
        return

    keys = []
    pendingBoxes = []

    for index, box in enumerate(boxes):
        if index in keys or index == 0:
            for newkey in box:
                if newkey and newkey not in keys:
                    keys.append(newkey)
        else:
            pendingBoxes.append(index)
        for key in keys:
            if key in pendingBoxes:
                for newkey in boxes[key]:
                    if newkey and newkey not in keys:
                        keys.append(newkey)
                pendingBoxes.remove(key)

    if len(pendingBoxes) > 0:
        return False
    return True
