#!/usr/bin/python

class Queue:
    def __init__(self):
        self.queue = []

    def push(self,value):
        self.queue.insert(0,value)

    def pop(self):
        return self.queue.pop()

    def show(self):
        print self.queue

    def isNotEmpty(self):
        return len(self.queue) != 0

    def length(self):
        return len(self.queue)
