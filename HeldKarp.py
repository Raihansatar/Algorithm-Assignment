import itertools


# function of travel salesman person using Held-Karp algorithm
def TSP(location):
    n = len(location)

    # initial value of 0 to all other points
    A = {}
    for i, cost in enumerate(location[0][1:]):  # w[0][1:] = take length start from [0][1 afterward]
        A.update({
            (frozenset([0, i + 1]), i + 1): (cost, [0, i + 1])
        })

    for m in range(2, n):  # n, is the length of matrix
        B = {}

        # At this stage the recursion is used, in addition the 'combinations' module is used, which allows grouping
        # and comparing data.
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, n), m)]:
            for j in S - {0}:  # create set with all the place
                # The least expensive route for the trip is sought, that is, the minimum values ​​are sought.
                B[(S, j)] = min(
                    (A[(S - {j}, k)][0] + location[k][j], A[(S - {j}, k)][1] + [j]) for k in S if k != 0 and k != j)

        A = B  # store B in as as B in the loop only
    # Start path and end path are now added

    res = min((A[d][0] + location[0][d[1]], A[d][1]) for d in iter(A))  # get the minimum from the last set
    # store res in array
    # Once the minimum value is found, the optimal solution is available.

    result = res[0], [(i) for i in res[1]]
    result[1].append(0)

    return result
# End of travel salesman person function
