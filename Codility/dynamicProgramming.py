import sys


def solution(A):
    dp = [0] * len(A)
    dp[0] = A[0]

    for i in range(1, len(A)):
        maxVal = -sys.maxsize - 1

        for k in range(1, 7):
            if i - k >= 0:
                maxVal = max(maxVal, dp[i - k] + A[i])

        dp[i] = maxVal
    return dp[len(A) - 1]


print(solution([1, -2, 0, 9, -1, -2]))
