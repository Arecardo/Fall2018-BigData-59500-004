#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys

current_hostname = None
current_filename = None
hostname = None
filename = None
count = 1

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    hostname, filename = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # by key (here: word) before it is passed to the reducer
    if current_hostname == hostname and current_filename != filename:
        count += 1
    else:
        if current_hostname and current_hostname != hostname:
            # write result to ouput
            print('%s\t%s' % (current_hostname, count))
        count = 1
        current_hostname = hostname
        current_filename = filename

# put the last word into newDict{}
if current_hostname == hostname:
    print('%s\t%s' % (current_hostname, count))
