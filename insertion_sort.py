#!/usr/bin/python

#it works by taking elements from the list one by one and inserting
#them in their correct position into a new sorted list.

def insert_at_position(input,i,j):
    first = input[:i]
    first.append(input[j])
    first.append(input[i:j])
    first.append(input[j+1:])
    return first
def add_at_position(input,output,pos):
    return output + [input[pos]]

def insertion_sort(input):
    result = []
    for i in range(len(input)):
        result = add_at_position(input,result,input.index(min(input)))
        input.remove(min(input))
    return result

def insertion_sort_space_efficient(input):
    N = len(input)
    i = 1
    j = i-1
    for i in range(i,N):
        temp = input[i]
        extra = 0
        while (j >= 0) & (input[j] > temp):
            tmp = input[i]
            input.remove(tmp)
            input.insert(j,tmp)
            extra+=1
            j-=1
        j+=(extra+1)
    return input

temp = [23,124,24,85423,34,6432,23,62,90]
#print insertion_sort(temp)
print insertion_sort_space_efficient(temp)
