# TSP
# Autor: David Felipe Velez Cadavid
# Colaborador: Juan Manuel Vergara Alvarez

# Dynamic Programming
# https://www.tutorialspoint.com/design_and_analysis_of_algorithms/design_and_analysis_of_algorithms_travelling_salesman_problem.htm
# encoding: utf-8
import itertools

# In the first instance a 6x6 matrix is ​​created, this matrix is ​​asymmetric, this is because the costs to travel
# from city to city vary

w = [[0.0, 1178.671859673486, 1180.0700698191881, 3224.777990540157, 2508.4362660368365, 5318.677216353381,
      4332.215068712133, 4601.871799273804],
     [1178.671859673486, 0.0, 2312.509200540841, 3804.2538748562656, 3247.6059266254892, 5773.0987509953375,
      5195.7631594758395, 5274.932678827154],
     [1180.0700698191881, 2312.509200540841, 0.0, 2535.8957177665757, 1726.1824898477594, 4610.121572373538,
      3288.6020977412145, 3719.354478303037],
     [3224.777990540157, 3804.2538748562656, 2535.8957177665757, 0.0, 814.2973250648984, 2104.3130981577674,
      1718.2312737282152, 1480.973652900838],
     [2508.4362660368365, 3247.6059266254892, 1726.1824898477594, 814.2973250648984, 0.0, 2889.7150555266576,
      1965.7256268618175, 2093.6715546233295],
     [5318.677216353381, 5773.0987509953375, 4610.121572373538, 2104.3130981577674, 2889.7150555266576, 0.0,
      2104.349974804228, 1161.2277477992286],
     [4332.215068712133, 5195.7631594758395, 3288.6020977412145, 1718.2312737282152, 1965.7256268618175,
      2104.349974804228, 0.0, 955.7689217292318],
     [4601.871799273804, 5274.932678827154, 3719.354478303037, 1480.973652900838, 2093.6715546233295,
      1161.2277477992286, 955.7689217292318, 0.0]]


# Travel function: performs the necessary calculations through comparisons between travel costs, to go from city to
# city, storing respectively the minimum costs in lists.

def travel(w):
    n = len(w)

    # initial value of 0 to all other points
    # A = {(frozenset([0, i + 1]), i + 1): (cost, [0, i + 1]) for i, cost in enumerate(w[0][1:])}
    A = {}
    for i, cost in enumerate(w[0][1:]):  # w[0][1:] = take length start from [0][1 afterward]
        A.update({
            (frozenset([0, i + 1]), i + 1): (cost, [0, i + 1])
        })

    # print(A)

    # print()
    for m in range(2, n):  # n=4, is the length of matrix
        B = {}

        # At this stage the recursion is used, in addition the 'combinations' module is used, which allows grouping
        # and comparing data.

        # X = {}
        # for C in itertools.combinations(range(1, n), m): # c = combination using itertools, length and current
        #     S = [frozenset(C) | {0}]
        #     # put 0, combine 0 into C
        #     print(C)
        #     print(frozenset(C) | {0})

        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, n), m)]:
            for j in S - {0}:
                # The least expensive route for the trip is sought, that is, the minimum values ​​are sought.
                B[(S, j)] = min(
                    (A[(S - {j}, k)][0] + w[k][j], A[(S - {j}, k)][1] + [j]) for k in S if k != 0 and k != j)
        A = B
    # Start path and end path are now added

    res = min([(A[d][0] + w[0][d[1]], A[d][1]) for d in iter(A)])

    #
    # for d in iter(A):
    #     print(A[d][0] + w[0][d[1]], A[d][1])
    # Once the minimum value is found, the optimal solution is available.
    # print(res)

    Resultado = res[0], [(i) for i in res[1]]
    Resultado[1].append(0)
    # print(Resultado[1])
    # with the ordering of costs, it is only necessary to show which is the route to follow in the trip, that is to
    # say, the cities are positioned in relation to their costs.

    return Resultado


# location = ["Kuala Lumpur", "Jakarta", "Bangkok", "Taipei", "Hong Kong", "Tokyo", "Beijing", "Seoul"]
travel(w)
# print(travel(w)[1])
# print(travel(w)[0])

# print ("\nBest travel route with return to the city 1 is:\n", travel(w)[1], "\n\nWith cost total:\n", travel(w)[0])
