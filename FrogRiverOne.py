# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, A):
    # write your code in Python 2.6
    frog, leaves = 0, [False] * (X)
    for second, leaf in enumerate(A):
        if leaf <= X:
            leaves[leaf - 1] = True
        while leaves[frog]:
            frog += 1
            if frog == X:
                return second
    return -1
