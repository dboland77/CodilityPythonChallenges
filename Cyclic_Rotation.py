# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    # write your code in Python 3.6
    if A == []:
        return []

    if K == len(A):
        return A

    if K > len(A):
        K = K % len(A)

    B = A[len(A) - K : len(A) + 1]
    # B.reverse()
    A = A[: len(A) - K]

    return B + A


# The following issues have been detected: wrong answers.

# For example, for the input ([1, 1, 2, 3, 5], 42) the solution returned a wrong answer
# (got [1, 1, 2, 3, 5] expected [3, 5, 1, 1, 2]).

# A = [1, 1, 2, 3, 5]
# K = 42

# The following issues have been detected: runtime errors.

# For example, for the input ([], 1) the solution terminated unexpectedly.

print(solution([], 1))

