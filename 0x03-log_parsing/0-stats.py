#!/usr/bin/python3
"""A module that contains a script that reads stdin line by line and
computes metrics.
"""
import sys


total_size = 0
status_code_counts = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
    }
line_count = 0
flag = False


def print_stats(file_size, status_code_counts):
    """Prints the computed metrics to stdout.

    Args:
        file_size (int): The total file size.
        status_code_counts (dict): A dictionary containing the status
        codes and their counts.
    """
    global flag
    print("File size: {:d}".format(file_size))
    for key in sorted(status_code_counts.keys()):
        if status_code_counts[key] != 0:
            print("{:s}: {:d}".format(key, status_code_counts[key]))
    flag = True


try:
    for line in sys.stdin:
        line_count += 1
        split_line = line.split()
        if len(split_line) < 2:
            continue
        total_size += int(split_line[-1]) if split_line[-1].isdigit() else 0
        status_code = split_line[-2]
        if status_code in status_code_counts.keys():
            status_code_counts[status_code] += 1
            flag = False
        if line_count % 10 == 0:
            print_stats(total_size, status_code_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_code_counts)
    raise
finally:
    if not flag:
        print_stats(total_size, status_code_counts)
