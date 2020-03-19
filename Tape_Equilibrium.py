# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6

    if A == []:
        return 0

    if len(A) == 1:
        return abs(A[0])

    # Calculate the first partition sums
    P = 1
    left = A[0]
    right = sum(A[1 : len(A)])
    store_diff = abs(left - right)

    # We don't need to calculate any more sums - each time the marker moves
    # we add that number to the left and take it off the right
    for P in range(2, len(A)):
        left += A[P - 1]
        right -= A[P - 1]
        diff = abs(left - right)

        if diff < store_diff:
            store_diff = diff

    return store_diff

