#!/usr/bin/python3
import sys
import math
delta1 = int(0)
delta2 = int(0)
M2 = int(0)
variance = int(0)
(current_store, tot_sales, count) = (None, 0.0, int(0))
for line in sys.stdin:
    (store, sale) = line.split('\t')
    if current_store and store != current_store:
        print('%s\t%s' % (current_store, SD))
        delta1 = int(0)
        delta2 = int(0)
        M2 = int(0)
        variance = int(0)
        (current_store, tot_sales) = (store, float(sale))
        count = 1
    else:
        mean = tot_sales / (count + 1)
        delta1 = float(sale) - mean
        mean = mean + delta1 / (count + 1)
        delta2 = float(sale) - mean
        M2 = M2 + delta1 * delta2
        variance = M2 / (count + 1)
        SD = variance ** 0.5
        (current_store, tot_sales, count) = (store, tot_sales + float(sale), count + 1)
       # print('%s\t%s' % (current_store, SD))
     #   print('%s\t%s\t%s\t%s' % (current_store, tot_sales, SD, count))
if current_store:
    print('%s\t%s' % (current_store, SD))



