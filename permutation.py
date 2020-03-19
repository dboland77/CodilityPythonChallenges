# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6

    # An arithemtic sequence of length N with common difference 1 should have sum to N terms of
    # n/2 * [2a + (n-1)d]
    # here a = A[0], n = len(A) and d = 1

    if len(A) == 1:
        if A[0] == 1:
            return 1
        else:
            return 0

    # We can check distinct values quickly by adding to a set
    Set_Values = set(A)
    # If the values are disintct then the length of the set will equal the length of the array
    if len(Set_Values) != len(A):
        return 0
    # Sort in ascending order
    A.sort()
    if A[0] != 1:
        return 0

    if A[len(A) - 1] != len(A):
        return 0

    checksum = (len(A) / 2) * (2 * A[0] + (len(A) - 1) * 1)

    if checksum == sum(A):
        return 1
    else:
        return 0


A = [3, 2]
print(solution(A))
