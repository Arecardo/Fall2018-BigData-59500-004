#! /usr/bin/python3
import sys

x = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    attributes = line.split()
    #x = attributes[3].find('.gif')
    #y = attributes[3].find('.htm')
    #z = attributes[3].find('.xbm')
    #if x!= -1 or y!= -1 or z!= -1:
        #print('%s\t%s' % (attributes[0],attributes[3]))
    print('%s\t%s' % (attributes[0],attributes[3]))
