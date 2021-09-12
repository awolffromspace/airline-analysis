#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    print("{0},{1}".format(row[14], row[13]))
