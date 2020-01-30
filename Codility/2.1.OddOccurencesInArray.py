# Notes: considerate the situation when unpaired elements are more than one

# the largest integer we have to deal with
MAXINT = 1000000


def solution(A):
    """
    Find the value of the unpaired element of a non-empty odd sized array
    :param A: an non empty array of integers with an odd number of elements
    :return: the value of the unpaired element[int]
    """
    # protect against crazy inputs
    if not isinstance(A, list):
        raise TypeError("Input must be a list of integers")
    if len(A) < 1:
        raise ValueError("Input list must not be empty")
    if len(A) > MAXINT:
        raise ValueError("Input must be an array with less than 1,000,000 elements")
    if len(A) % 2 == 0:
        raise ValueError("Input must be an odd array")

    # initiate hash
    unmatched = {}

    # for every element
    for i, num in enumerate(A):
        if num not in unmatched.keys():
            unmatched[num] = i
        else:
            del unmatched[num]

    # whether only one unmatched item
    if len(unmatched) == 1:
        return unmatched.keys()[0]
    else:
        raise Exception("Expected one unmatched item, but have this: %s" % unmatched)


if __name__ == '__main__':
    # unittest.main()
    A = [9, 3, 9, 3, 9, 7, 5]
    print(solution(A))
