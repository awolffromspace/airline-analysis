#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    print("{0}\t{1}".format(row[1], row[12]))
