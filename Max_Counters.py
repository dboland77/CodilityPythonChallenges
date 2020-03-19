# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, A):
    # write your code in Python 3.6
    # Array A is M integers long and non-empty
    # The array represents consecutive operations
    # A[K] = X for 1 <=X<=N then K is increase(X) by 1
    # A[K] = N+1 then operation K is max counter setting all counters to the max value of any counter
    # N = number of counters all set to 0 initially
    # X represents the counter number (index)
    counters = N * [0]
    last_update = 0
    max_item = 0

    for item in A:
        #     # This line here is going to update the whole array
        #     # If all the operations in A were max item this would do this M times
        #     # giving N*M complexity
        #     if item == N+1:
        #         counters = N*[max_item]
        if item < N + 1:
            if counters[item - 1] < last_update:
                counters[item - 1] = last_update

            counters[item - 1] += 1

            if counters[item - 1] > max_item:
                max_item = counters[item - 1]
        else:
            last_update = max_item

    for i in range(len(counters)):
        if counters[i] < last_update:
            counters[i] = last_update

    return counters
