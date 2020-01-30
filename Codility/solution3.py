

def solution(A):
    """
    :param A: array, An array consisting of N integers
    :return: int, the number of identical pairs of indices
    """
    # A is an empty array or single element array
    if len(A) < 2:
        return 0

    # First, calculate the frequency of identical elements in a given array
    dicA = {}
    for i in range(len(A)):
        if A[i] in dicA.keys():
            dicA[A[i]] += 1
        else:
            dicA[A[i]] = 1

    # count pairs for each identical element
    counter = 0
    for count in list(dicA.values()):
        counter += (count * (count - 1)) / 2
    return int(counter)


import unittest
import random

MAXINT = 1000000000
MAXN = 1000000


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([3, 5, 6, 3, 3, 5]), 4)

    def test_simple(self):
        self.assertEqual(solution([0, -1, 3, 3]), 1)

    def test_extreme_small(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([1]), 0)
        self.assertEqual(solution([0, -1]), 0)

    def test_extreme_large(self):
        print(solution(random.sample(range(-MAXINT,MAXINT), MAXN)))


if __name__ == '__main__':
    unittest.main()

# # print(solution([3, 5, 6, 3, 3, 5]))
# print(solution([3, 5, 6, 7, -2, -5]))
