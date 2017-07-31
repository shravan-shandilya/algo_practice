#!/usr/bin/python
def swap(input,i,j):
    if input[i] > input[j]:
        input[i],input[j]=input[j],input[i]

def bubble_sort(input):
    i = 0
    while i < len(input)-i:
        j = 0
        while j < len(input)-1:
            swap(input,j,j+1)
            j = j + 1
        i = i + 1
    return input

temp = [23,5322,53,532,563,23,6,31,7432,865,34,224]
print bubble_sort(temp)
