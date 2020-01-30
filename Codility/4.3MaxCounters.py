# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def slow_solution(N, A):
    counter = [0] * N

    for X in A:
        if X == N + 1:
            counter = [max(counter)] * N
        else:
            counter[X - 1] += 1

    return counter


def solution(N, A):
    """
    :param N: integer - the number of counters
    :param A: a sequence of integers specifying which counter to increase
    :return: the list of counters' values
    """
    counters = [0] * (N + 1)  # make it one longer so the counter number works as an index without being off by one
    maximum = 0
    minimum = 0

    # step through the array of instructions
    for key in A:
        if key <= N:
            # align with the minimum
            if counters[key] < minimum:
                counters[key] = minimum
            # now increment it
            counters[key] += 1
            # update the maximum
            if counters[key] > maximum:
                maximum = counters[key]
        else:
            # an update-all instruction resets the minimum
            minimum = maximum

    # set any counters below the minimum to the minimum
    for key, value in enumerate(counters):
        if value < minimum:
            counters[key] = minimum

    return counters[1:]  # trim the zero array position off


solution(5, [3, 4, 4, 6, 1, 4, 4])
