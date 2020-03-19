# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    if A == []:
        return 1

    A.sort()

    if len(A) == 1:
        if A[0] != 1:
            return 1
        else:
            return 2

    if A[len(A) - 1] < 0:
        return 1

    if A[0] > 0 and A[0] != 1:
        return 1

    for i in range(len(A)):
        if i == len(A) - 1:
            if A[len(A) - 2] > 0:
                return A[len(A) - 1] + 1
            else:
                return 1

        if (A[i + 1] != A[i] + 1) and (A[i + 1] != A[i]) and (A[i] > 0):
            return A[i] + 1
