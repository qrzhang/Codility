# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    """
    :param X: 
    :param A: array consisting of integers
    :return: 
    """
    number = len(A)
    if number < X or max(A) < X:
        return -1

    dic_leaf = {}
    count = 0
    for time in range(number):
        if A[time] not in dic_leaf.keys():
            dic_leaf[A[time]] = 1
            count += 1
            if count == X:
                return time
    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))