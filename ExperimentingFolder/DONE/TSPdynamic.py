# TSP
# Autor: David Felipe Velez Cadavid
# Colaborador: Juan Manuel Vergara Alvarez

# Dynamic Programming
# Held-Karp Algorithm

import itertools

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
    A = {}
    for i, cost in enumerate(w[0][1:]):  # w[0][1:] = take length start from [0][1 afterward]
        A.update({
            (frozenset([0, i + 1]), i + 1): (cost, [0, i + 1])
        })

    for m in range(2, n):  # n=4, is the length of matrix
        B = {}

        # At this stage the recursion is used, in addition the 'combinations' module is used, which allows grouping
        # and comparing data.
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, n), m)]:
            for j in S - {0}: # create set with all the place
                # The least expensive route for the trip is sought, that is, the minimum values ​​are sought.
                B[(S, j)] = min(
                    (A[(S - {j}, k)][0]+w[k][j], A[(S - {j}, k)][1] + [j]) for k in S if k != 0 and k != j)

        A = B  # store B in as as B in the loop only
    # Start path and end path are now added

    res = min((A[d][0] + w[0][d[1]], A[d][1]) for d in iter(A))  # take the minimum from the last set
    # store res in array
    # Once the minimum value is found, the optimal solution is available.
    # print(res)

    Resultado = res[0], [(i) for i in res[1]]
    Resultado[1].append(0)
    print(Resultado[1])
    print(Resultado[0])

    return Resultado

travel(w)
