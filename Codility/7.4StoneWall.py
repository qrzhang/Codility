import unittest
import random

RANGE_INT = (1, 1000000000)
RANGE_N = (1, 100000)


def solution(H):
    current = None
    counter = 1
    for i in range(len(H)):
        previous = current
        current = H[i]
        if previous:
            if current != previous:
                counter += 1
    return counter


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]), 7)

    def test_simple(self):
        self.assertEqual(solution([1, 3, 1]), 3)

    def test_extreme_small(self):
        self.assertEqual(solution([1]), 1)
        self.assertEqual(solution([10]), 1)
        self.assertEqual(solution([1, 1]), 1)


if __name__ == '__main__':
    unittest.main()
# print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
