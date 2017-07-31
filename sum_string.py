#!/usr/bin/python
def sum_string(str):
    for i in range(len(str)-2):
        if int(str[i])+int(str[i+1]) == int(str[i+2]):
            continue
        else:
            return False
    return True

print sum_string("1234566324")
print sum_string("12358")
print sum_string("112358")
print sum_string("01123")
print sum_string("123234134124")
