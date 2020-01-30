import math


def iteration(counter, i, A, dicA):
    """
    :param counter: int, save length of current linked List
    :param i: int, iteration variable
    :param A: A non-empty array
    :param dicA: dictionary, save the index that we have passed before
    :return: next iteration or counter
    """
    # If one index appears before, should return Inf
    if A[i] in dicA.keys():
        return math.inf
    # save current index
    dicA[A[i]] = 1
    # update counter
    counter += 1

    if A[i] == -1:
    # when reach the end of linked list
        return counter
    else:
    # Still need next iteration
        return iteration(counter, A[i], A, dicA)


def solution(A):
    """
    :param A: A non-empty array
    :return: the length of that linked list represented by A
    """
    counter = 0
    dicA = {}
    return iteration(counter, 0, A, dicA)




import unittest
import random

RANGE_INT = (1, 200000)
RANGE_N = (1, 100000)


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([1, 4, -1, 3, 2]), 4)

    def test_simple(self):
        self.assertEqual(solution([0]), math.inf)
        self.assertEqual(solution([2,1,3,-1]), 3)

    def test_extreme_small(self):
        self.assertEqual(solution([0]), math.inf)
        self.assertEqual(solution([-1]), 1)
        self.assertEqual(solution([1,-1]), 2)
        self.assertEqual(solution([1, 3, -1, 3, 0, -1]), math.inf)


if __name__ == '__main__':
    unittest.main()
    # print(solution([1, 4, -1, 3, 2]))
    # print(solution([1, 3, -1, 3, 0, -1]))
