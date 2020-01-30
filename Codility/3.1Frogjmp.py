# the largest integer we have to deal with
MAXINT = 1000000000


def solution(X, Y, D):
    # write your code in Python 3.6
    """
    count the minimal number of jumps that the small frog must perform to reach its target
    :param X: [int] currently location of the frog
    :param Y: [int] target position
    :param D: [int] a fixed distance the frog can jump
    :return: [int] minimal number of jumps
    """
    # protect against crazy inputs
    if not isinstance(X, int):
        raise TypeError("Input X must be an integer")
    if not isinstance(Y, int):
        raise TypeError("Input Y must be an integer")
    if not isinstance(D, int):
        raise TypeError("Input D must be an integer")
    if X > MAXINT or X < 1:
        raise ValueError("Input X must be a positive integer less than 1,000,000,000")
    if Y > MAXINT or Y < 1:
        raise ValueError("Input Y must be a positive integer less than 1,000,000,000")
    if D > MAXINT or D < 1:
        raise ValueError("Input D must be a positive integer less than 1,000,000,000")
    if X > Y:
        raise ValueError("Input X must be a integer less than or equal to integer Y")

    if X == Y:
        return 0

    gap = Y - X
    if gap % D == 0:
        return gap // D
    else:
        return gap // D + 1


if __name__ == '__main__':
    print(solution(10, 20, 3))
