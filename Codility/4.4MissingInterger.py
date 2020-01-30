def solution(A):
    # write your code in Python 3.6
    if max(A) <= 0:
        return 1

    num = max(A)
    counter = [0] * (num)

    for element in A:
        if element > 0:
            counter[element - 1] += 1

    for i, element in enumerate(counter):
        if element == 0:
            return i + 1
    return max(A) + 1