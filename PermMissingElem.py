# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    if A == []:
        return 1

    A.sort()

    # Check the first element
    if A[0] != 1:
        return 1

    # Check the last element
    if A[len(A) - 1] != len(A) + 1:
        return len(A) + 1

    for i in range(0, len(A)):
        bCheck = A[i] == A[0] + i
        if not bCheck:
            # If this fails the missing element is one less than this element
            return A[i] - 1
