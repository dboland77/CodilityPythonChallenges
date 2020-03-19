def solution(A):
    min_idx = 0
    min_value = 10001

    for idx in range(0, len(A) - 1):
        if (A[idx] + A[idx + 1]) / 2.0 < min_value:
            min_idx = idx
            min_value = (A[idx] + A[idx + 1]) / 2.0
        if idx < len(A) - 2 and (A[idx] + A[idx + 1] + A[idx + 2]) / 3.0 < min_value:
            min_idx = idx
            min_value = (A[idx] + A[idx + 1] + A[idx + 2]) / 3.0

    return min_idx
