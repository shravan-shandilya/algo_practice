#!/usr/bin/python
def merge(t1,t2):
    n1,n2 = len(t1),len(t2)
    i,j = 0,0
    temp = []
    while (i < n1) & (j < n2):
        if t1[i] <= t2[j]:
            temp.append(t1[i])
            i = i + 1
        else:
            temp.append(t2[j])
            j = j + 1
    while i < n1:
        temp.append(t1[i])
        i = i + 1
    while j < n2:
        temp.append(t2[j])
        j = j + 1
    return temp

def merge_sort(input):
    if len(input) < 2:
        return input
    temp1 = input[:len(input)/2]
    temp2 = input[len(input)/2:]
    return merge(merge_sort(temp1),merge_sort(temp2))

print merge_sort([2,7,8,1,5,6,8])
