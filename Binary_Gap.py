# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # write your code in Python 3.6
    bin_num = bin(N)[2:]
    bin_gap = 0
    store_gap = 0
    start_gap = False
    end_gap = False

    for i in range(len(bin_num) - 1, -1, -1):
        if bin_num[i] == "0":
            bin_gap += 1
        if bin_num[i] == "1":
            if not start_gap:
                start_gap = True
            else:
                start_gap = False
                end_gap = True
            if bin_gap > store_gap:
                if end_gap:
                    store_gap = bin_gap
            bin_gap = 0

    return store_gap
