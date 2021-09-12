#!/usr/bin/env python3

from operator import itemgetter
import sys

current_reason = None
current_count = 0
reason = None

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    canceled = "0"
    try:
        reason = line[0]
        canceled = line[1]
    except IndexError:
        continue

    if canceled == "0":
        continue

    if current_reason == reason:
        current_count += 1
    else:
        if current_reason:
            print("{0}\t{1}".format(current_reason, current_count))
        current_reason = reason
        current_count = 1

if current_reason == reason:
    print("{0}\t{1}".format(current_reason, current_count))
