import unittest
import random

RANGE_A = (0, 2147483647)
RANGE_N = (0, 100000)
MAX_INTERSECTIONS = 10000000


def fast_solution(A):
    """
    100% O(N*log(N))
    Take advantage of the fact that, for accounting purposes, it isn't necessary to keep specific
    opening and closing points together.  We only need to know how many discs are open when a disc
    closes.  Thus we can step through all the closing points and simply count the
    number of discs that have opened since the last close.
    """
    # create separate lists of all the start points and the end points, and sort them
    starts, ends = [], []
    for point, radius in enumerate(A):
        starts.append(point - radius)
        ends.append(point + radius)
    starts.sort()
    ends.sort()

    # every time a disc closes we add an intersection for every disc that has opened
    # since the last close
    intersections = istart = 0
    for iend in range(len(ends)):                                          # for every closing
        while istart < len(starts) and starts[istart] <= ends[iend]:        # step through unreconciled openings
            istart += 1
        intersections += istart - iend - 1                                  # and record them as intersections

        # trap runaway monsters
        if intersections > MAX_INTERSECTIONS:
            return -1

    return intersections


solution = fast_solution


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)

    def test_simple(self):
        self.assertEqual(solution([1, 1, 1]), 3)  # this is not 5, but 3!

    def test_extreme_small(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([10]), 0)
        self.assertEqual(solution([1, 1]), 1)

    def test_extreme_large(self):
        A = [10000000] * 100000
        self.assertEqual(solution(A), -1)


if __name__ == '__main__':
    unittest.main()