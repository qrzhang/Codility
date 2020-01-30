def solution(A):
    # write your code in Python 3.6
    num = len(A)
    maxSum = (num + 1) * (num + 2) // 2
    missing = maxSum - sum(A)

    return int(missing)

print(solution([2,3,1,5]))