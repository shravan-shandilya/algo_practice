#!/usr/bin/python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def show(self):
        print self.stack

    def empty(self):
        return len(self.stack) == 0

    def top(self):
        if not self.empty():
            return self.stack[len(self.stack)-1]
        else:
            return None
