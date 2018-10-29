#! /usr/bin/python3

import sys

# This function is used to handle double quote, single quote,
#or other non-alphabet character in the prefix or suffix.

#at first i tried to handle words
#however, i found that it can't handle some specific alphas like "--" and "://"
#def handle_word(word):
    #word = word.replace('"','')
    #word = word.replace('.','')
    #word = word.replace(',','')
    #x = word.find('--')
    #if x != -1:
        #newWord = word.split('--')
        #for word in newWord:
            #print('%s\t%s' % (word, 1))
    #else:
        #print('%s\t%s' % (word, 1))

#so, i turned to try to handle lines
#and it works well
def handle_line(line):
    line = line.replace('"',' ')
    line = line.replace('.',' ')
    line = line.replace(',',' ')
    line = line.replace('://',' ')
    line = line.replace(':',' ')
    line = line.replace('--',' ')
    line = line.replace('-',' ')
    line = line.replace('@',' ')
    line = line.replace('(',' ')
    line = line.replace(')',' ')
    line = line.replace('$',' ')
    line = line.replace("'",' ')
    line = line.replace("!",' ')
    line = line.replace(";",' ')
    line = line.replace("_",' ')
    line = line.replace("?",' ')
    line = line.replace("[",' ')
    line = line.replace("]",' ')
    line = line.replace("/",' ')
    line = line.replace("{",' ')
    line = line.replace("}",' ')
    line = line.replace("^",' ')
    return line

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = handle_line(line)
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        word = word.lower()
        print('%s\t%s' % (word, 1))
