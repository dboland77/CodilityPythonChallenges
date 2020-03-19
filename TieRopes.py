# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(K, A):
    cnt = 0
    current = 0
    for part in A:
        current += part
        if current >= K:
            cnt += 1
            current = 0

    return cnt
