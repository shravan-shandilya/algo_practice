#!/usr/bin/python

def max_diff_in_increasing_order(data):
    minimum = data.index(min(data))
    print minimum,data[minimum]
    max_diff = 0
    for i in range(minimum,len(data)-1):
        diff = data[i] - data[minimum]
        print diff,max_diff
        if diff > max_diff:
            max_diff =max_diff
    return max_diff

print max_diff_in_increasing_order([3,2,1,4,6,3,6,2,5,6,9])
