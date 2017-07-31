#!/usr/bin/python
def swap(input,i,j):
    input[i],input[j]=input[j],input[i]

def quick_sort(input,start,end):
    if start < end:
        pivot = partition(input,start,end)
        quick_sort(input,start,pivot-1)
        quick_sort(input,pivot+1,end)
    return input

def partition(input,start,end):
    pivot = start
    left = start + 1
    right = end
    while left < right:
        while (input[left] < input[pivot]) & (left < end):
            left = left + 1
        while (input[right] > input[pivot]) & (right > start):
            right = right - 1
        swap(input,left,right)
        left = left + 1
        right = right - 1
    swap(input,pivot,min(left,right))
    return min(left,right)


temp = [3,5,2,6,7,3,4,1,0]
print quick_sort(temp,0,len(temp)-1)
