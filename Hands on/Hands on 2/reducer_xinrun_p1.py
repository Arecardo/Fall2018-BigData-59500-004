#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
newDict = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to newDict{}
            newDict[current_word] = current_count
        current_count = count
        current_word = word

# put the last word into newDict{}
if current_word == word:
    newDict[current_word] = current_count

#sort the newDict{} and put the result into sorted_Dict{}
#output top 10 values and keys
sorted_Dict = sorted(newDict.items(),key = lambda item:item[1],reverse = 1)
m = 0
while m < 10:
    print(sorted_Dict[m])
    m += 1
