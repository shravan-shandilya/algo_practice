def solution(N):
    # write your code in Python 2.7
    max = 0
    while N != 0:
        zeroes = 0
        if N&1 != 1:
            while N&1 != 1 and N != 0 and N != 1:
                zeroes += 1
                N = N >> 1
            if zeroes > max:
                max = zeroes
        else:
            N = N >> 1
    return max
print solution(529)
