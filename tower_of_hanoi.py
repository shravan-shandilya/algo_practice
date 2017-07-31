#!/usr/bin/python

def print_tower(src,aux,dst):
    print "########################"
    print "Source:",src
    print "Auxilary:",aux
    print "Destination:",dst

def hanoi(n,src,aux,dst):
    if n > 0:
        hanoi(n-1,src,dst,aux)
        if src:
            dst.append(src.pop())
        hanoi(n-1,aux,src,dst)

src = [4,3,2,1]
dst = []
aux = []

print_tower(src,aux,dst)
hanoi(len(src),src,aux,dst)

print_tower(src,aux,dst)
