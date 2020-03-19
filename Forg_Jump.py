# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y, D):
    # write your code in Python 3.6
    Jumps = (Y - X) // D
    Remainder = (Y - X) % D

    if Remainder > 0:
        Jumps += 1

    return Jumps
