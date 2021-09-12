#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    print("{0},{1},{2}\t{3}".format(row[1], row[4], row[8], row[12]))
