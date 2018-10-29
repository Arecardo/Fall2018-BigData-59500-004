#!/usr/bin/python3
import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split('\t')
    store = words[2]
    sale = words[4]
    print('%s\t%s' % (store, sale))
