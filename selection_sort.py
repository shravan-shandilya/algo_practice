#!/usr/bin/python

#The algorithm finds the minimum value,
#swaps it with the value in the first position,
#and repeats these steps for the remainder of the list.

def swap(input,i,j):
    input[i],input[j] = input[j],input[i]

def index_of_min(input,start,end):
    min = start
    for i in range(start,end):
        if input[i] < input[min]:
            min = i
    return min

def selection_sort(input):
    for i in range(0,len(input)):
        swap(input,i,index_of_min(input,i,len(input)))
    return input

temp = [34, 234, 89,12,653,1235,7562,23,73,215]
#temp = [23,23,5213,54,123,7546,234,86756,1233]
print selection_sort(temp)


#Complexity analysis
# n = size of array

#selection_sort calls swap 'n'times.
#time = n * (time taken by swap + time taken by index_of_min)

#time taken by swap = 4 memory access

#time taken by index_of_min = 2 * sigma over (i,n) of (n-i)

# total_time = n * (4 + 2(n(n+1)/2))
# total_time = n * (4 + n^2+ n)
