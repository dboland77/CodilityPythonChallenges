def solution(A):
    return len(set(A))


def solution(A):
    if len(A) == 0:
        return 0

    A.sort()

    nr_values = 1
    last_value = A[0]

    for idx in range(1, len(A)):
        if A[idx] != last_value:
            nr_values += 1
            last_value = A[idx]

    return nr_values
