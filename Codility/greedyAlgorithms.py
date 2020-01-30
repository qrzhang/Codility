def greedyCoinChanging(M, k):
    n = len(M)
    result = []
    for i in range(n - 1, -1, -1):
        result += [M[i], k // M[i]]
        k %= M[i]
    return result


print(greedyCoinChanging([1, 3, 4], 6))



