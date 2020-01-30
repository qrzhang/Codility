# Notes: considerate the situation when K is larger than the length of input array

# the largest integer we have to deal with
MAXITERATION = 100
MAXINT = 1000

# simpiest way
def my_solution(A, K):
    """
    Rotate an array K times
    :param A: an non empty array of integers
    :return: an array after being rotated K times
    """
    # protect against crazy inputs
    if not isinstance(A, list):
        raise TypeError("Input A must be a list of integers")
    if not isinstance(K, int):
        raise TypeError("Input K must be a integer")
    if A is None:
        raise ValueError("Input list must not be None")
    if K > MAXINT:
        raise ValueError("Iteration must less than 100 times")
    # if input list is empty or only contain 1 element, the result should be itself all the time
    if not len(A):
        return A

    num = len(A)
    shift = K % num
    part1 = A[:num - shift]
    part2 = A[num - shift:]
    return part2 + part1


if __name__ == '__main__':
    print(my_solution([1,1,2,3,5], 6))
