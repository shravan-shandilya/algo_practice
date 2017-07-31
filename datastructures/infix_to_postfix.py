#!/usr/bin/python
import stack
precedence = {}
precedence["+"] = 1
precedence["-"] = 1
precedence["*"] = 2
precedence["/"] = 2
precedence["("] = 0

def precedence_adjust(minimum,maximum):
    return precedence[minimum] <= precedence[maximum]

def infix_to_postfix(expr):
    postfix = []
    ops = stack.Stack()
    for index in range(len(expr)):
        element = expr[index]
        if element in "ABCDE":
            postfix.append(element)
        elif element == ")":
            while element != "(":
                element = ops.pop()
                postfix.append(element)
        elif element in "+-*/(":
            while (not ops.empty()) and precedence_adjust(element,ops.top()):
                postfix.append(ops.pop())
            ops.push(element)
        else:
            print "problem",element
    while not ops.empty():
        postfix.append(ops.pop())
    return postfix

print infix_to_postfix("A+B")
print infix_to_postfix("A+B-C")
print infix_to_postfix("A+B*C-D")           #ABC*+D-
print infix_to_postfix("(A+B)*(C-D*E)")     #Not working
