def solution(A, K):
    # write your code in Python 2.7
    if K == 0:
        return A
    else:
        A = A[len(A)-1:]+ A[:len(A)-1]
        solution(A,K-1)
print solution([3, 8, 9, 7, 6], 3)
