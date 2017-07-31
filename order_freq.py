#!/usr/bin/python
def custom_print(value,times):
    while times != 0:
        print value
        times -= 1

def frequency_sorting(data):
    freq = ()
    for element in data:
        if not element in freq:
            freq[element] = (1,element)
        else:
            freq[element][1] += 1
    print freq
    #sorted_freq = sorted(freq.values(),key=lambda key: )
    #print sorted_freq

frequency_sorting([1,1,1,1,1,2,2,4,4,4,4,3,5,5,5,7,7,7,3,5,6,8,2])
