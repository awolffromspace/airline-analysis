#!/usr/bin/env python3

from operator import itemgetter
import sys

current_airline = None
current_sum = 0
current_count = 0
airline = None

for line in sys.stdin:
    line = line.strip()
    line = line.split("\t", 1)

    delay = 0
    try:
        airline = line[0]
        delay = line[1]
    except IndexError:
        continue

    try:
        delay = float(delay)
    except ValueError:
        continue

    if current_airline == airline:
        current_sum += delay
        current_count += 1
    else:
        if current_airline:
            print("{0}\t{1}".format(current_airline, current_sum / current_count))
        current_airline = airline
        current_sum = delay
        current_count = 1

if current_airline == airline:
    print("{0}\t{1}".format(current_airline, current_sum / current_count))
