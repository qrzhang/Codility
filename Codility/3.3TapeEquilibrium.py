def slow_solution(A):
    min_diff = abs(A[0] - sum(A[1:]))
    for p in range(2, len(A)-1):
        diff = abs(sum(A[:p]) - sum(A[p:]))
        if diff < min_diff:
            min_diff = diff
    return min_diff


def solution(A):
    min_diff = None
    head = 0
    tail = sum(A)
    for p in range(0,len(A) -1):
        head += A[p]
        tail -= A[p]
        if min_diff is None or abs(head - tail) < min_diff:
            min_diff = abs(head - tail)
    return min_diff


import random
N_RANGE = (2, 100000)
N = random.randint(*N_RANGE)

# slow_solution([3, 1, 2, 4, 3])
solution([3, 1, 2, 4, 3])
