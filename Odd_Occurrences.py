# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]

    A.sort()

    for i in A:
        if i % 2 != 0:
            if A[i] != A[i - 1]:
                return A[i - 1]

    return A[len(A) - 1]


# if i = 1 just return that element
# If we sort the array then the pairs will be beside each other with one not
# the second we find an element not followed by a match we return that and break
