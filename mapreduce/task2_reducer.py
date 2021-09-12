#!/usr/bin/env python3

from operator import itemgetter
import sys

current_airline = None
current_route = None
current_sum = 0
current_count = 0
route = None
airline = None

for line in sys.stdin:
    line = line.strip()

    delay = 0
    try:
        line, delay = line.split("\t", 1)
        delay = float(delay)
    except ValueError:
        continue

    line = line.split(",")

    try:
        airline = line[0]
        route = line[1] + "\t" + line[2]
    except IndexError:
        continue

    if airline != "B6" and airline != "G4" and airline != "MQ":
        continue

    if current_airline == airline and current_route == route:
        current_sum += delay
        current_count += 1
    else:
        if current_airline and current_route:
            print("{0}\t{1}\t{2}".format(current_airline, current_route, current_sum / current_count))
        current_airline = airline
        current_route = route
        current_sum = delay
        current_count = 1

if current_airline == airline and current_route == route:
    print("{0}\t{1}\t{2}".format(airline, current_route, current_sum / current_count))
