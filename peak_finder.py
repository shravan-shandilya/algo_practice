#!/usr/bin/python

def peak_finder(input):
    temp = len(input)/2
    if (temp != 0) and (temp != len(input)-1):
        if (input[temp-1] < input[temp]) & (input[temp] > input[temp+1]):
            return input[temp]
        elif (input[temp-1] > input[temp]) & (input[temp] > input[temp+1]):
            peak_finder(input[:temp])
        elif (input[temp-1] < input[temp]) & (input[temp] < input[temp+1]):
            peak_finder(input[temp:])

test = [2,3,4,5,6,7,8,9,100,7,6,5]
print peak_finder(test)
