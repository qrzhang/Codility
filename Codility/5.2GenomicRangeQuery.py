# impact factor of each neucleotide
M = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

def slow_solution(S, P, Q):
    """
    An easy to implement and understand solution: O(N * M)
    :param S: a string of 1..MAX_N chars containing a mix of the four chars A, C, G, and T
    :param P: a list of integers indexing a position in S
    :param Q: a list of integers indexing a position in S
    :return: a list of ints between 1 and 4, one for each query
    https://codility.com/demo/results/trainingC9QT9A-BQS/
    """
    # for every query, sort the sequence slice into alphabetical order: the first char will be the minimal-factor
    result = []
    for p, q in zip(P, Q):
        slice = sorted(S[p:q+1])
        result.append(M[slice[0]])
    return result

def fast_solution(S, P, Q):
    """
    A faster, but more difficult to implement and understand, solution: 0(N + M)
    :param S: a string of 1..MAX_N chars containing a mix of the four chars A, C, G, and T
    :param P: a list of integers indexing a position in S
    :param Q: a list of integers indexing a position in S
    :return: a list of ints between 1 and 4, one for each query
    """
    # Pass 1: Create suffix sums
    # We build four lists, one for each nucleo, which are as long as the sequence itself (plus one).
    # The lists preserve the sequence order and track the sum total of how many times we've seen that
    # nucleo type as we progress through the list.
    # Eg: The sum for "C" in "CAGCCTA" are [0,1,1,1,2,3,3,3]
    sumA = [0]; sumC = [0]; sumG = [0]; sumT = [0]
    for nuke in S:
        # copy the counts in the last cell into this one
        for sum in (sumA, sumC, sumG, sumT):
            sum.append(sum[-1])
        # increment the sum corresponding to the current nuke
        if nuke == 'A':
            sumA[-1] += 1
        elif nuke == 'C':
            sumC[-1] += 1
        elif nuke == 'G':
            sumG[-1] += 1
        else:
            sumT[-1] += 1

    # Pass 2: Evaluate the queries
    # Each query defines a slice via indicies P and Q which correspond to the start and end points.
    # By comparing the sum at both points we can readily determine how many nucleos of that type
    # appear within them.
    # Eg: In the sum [0,1,1,1,2,3,3,3], at index 2 there is a 1, and at index 4, there is a 2.
    # Thus, somewhere between indexes 2 and 4, there must have been a nucleo of type 'C'.
    # Additionally, we can determine how many 'C' nucleos are there by subtracting one sum from the other (2-1=1).
    impact = []
    for p, q in zip(P, Q):
        if sumA[q+1] > sumA[p]:
            impact.append(M['A'])
        elif sumC[q+1] > sumC[p]:
            impact.append(M['C'])
        elif sumG[q + 1] > sumG[p]:
            impact.append(M['G'])
        else:
            impact.append(M['T'])
    return impact





fast_solution('CAGCC', [2, 3, 0], [4, 1, 4])
