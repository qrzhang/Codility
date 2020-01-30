
def solution(A):
    """
    :param A: an array contains integers
    :return: return the abs value of max paired integers
    """
    dicA = {}
    maxPair = 0
    for item in A:
        if abs(item) in dicA.keys():
            if item == -dicA[abs(item)] and abs(item) > maxPair:
                maxPair = abs(item)
        else:
            dicA[abs(item)] = item
    return maxPair


import unittest
import random

MAXINT = 1000000000
MAXN = 100000


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([3, 2, -2, 5, -3]), 3)
        self.assertEqual(solution([1, 1, 2, -1, 2, -1]), 1)
        self.assertEqual(solution([1, 2, 3, -4]), 0)

    def test_simple(self):
        self.assertEqual(solution([2,1,3,-1]), 1)

    def test_extreme_small(self):
        self.assertEqual(solution([1]), 0)
        self.assertEqual(solution([0, -1]), 0)

    def test_extreme_large(self):
        # print(solution(random.sample(RANGE_INT, MAXN)))
        print(solution(random.sample(range(-MAXINT,MAXINT), MAXN)))


if __name__ == '__main__':
    unittest.main()