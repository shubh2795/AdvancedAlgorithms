# m is number of objects and n is size
import numpy as np

global weights


def weights_generator(M, avg_size):
    rand_weights = np.random.randint(1, 2 * avg_size + 1, M)
    # print(rand_weights)
    return rand_weights


def knapsack_recursive(m, n):
    global weights
    if n == 0:
        return True
    # -1 as I'm dealing with index and weights[0] is valid
    if m == -1:
        return False
    # overfilled knapsack
    if weights[m] > n:
        return knapsack_recursive(m - 1, n)

    else:
        return (knapsack_recursive(m - 1, n - weights[m]) or knapsack_recursive(
            m - 1, n))


def knapsack_memoization(m, n, cache):
    global weights
    if n == 0:
        return True
        # -1 as I'm dealing with index and weights[0] is valid
    if m == -1:
        return False
    if cache[n][m]:
        return cache[n][m]
    if weights[m] > n:
        res = knapsack_memoization(m - 1, n, cache)
        cache[n][m] = res
        return res
    else:
        res = knapsack_memoization(m - 1, n - weights[m], cache) or knapsack_memoization(
            m - 1, n, cache)
        cache[n][m] = res
        return res


def knapsack_DP(m, n):
    global weights
    cache = [[False for i in range(0, m + 1)] for j in range(0, n + 1)]
    # base cases
    for x in range(0, m + 1):
        cache[0][x] = True
    for i in range(1, m + 1):
        for j in range(0, n + 1):
            if weights[i - 1] > j:
                cache[j][i] = cache[j][i - 1]
            else:
                cache[j][i] = cache[j - weights[i - 1]][i - 1] or cache[j][i - 1]
    return cache[n][m]


def testMemoandDp():
    global weights
    m = len(weights)
    n = 1000
    print(knapsack_DP(m, n))


def test_case_point_6():
    global weights
    weights = weights_generator(10, 12)
    for i in range(1, 101):
        m = len(weights)
        n = 20
        # global cache: any variable declared outside the method(as per the definitions on google)
        cache = [[False for i in range(0, m + 1)] for j in range(0, n + 1)]
        a = knapsack_DP(m, n)
        b = knapsack_memoization(m - 1, n, cache)
        if (a != b):
            print("Failed: Output of DP and Memo function is different")
    print("Both the methods return same output for the test cases")


import time
import matplotlib.pyplot as plt


def showTime(function, function2, cache):
    global weights
    timeLine1 = []
    timeLine2 = []
    values = []
    # 10 aveSizes between 1 - 30000
    for i in range(1, 11):
        avgSize = 3000 * i
        start_time = time.time()
        ## 20 random size arrays
        for j in range(1, 21):
            m = 800
            weights = weights_generator(m, avgSize)
            n = 5000
            function(m, n)
        elapsed1 = (time.time() - start_time) * 1000.0 / 20

        start_time = time.time()
        for j in range(20):
            m = 800
            weights = weights_generator(m, avgSize)
            n = 5000
            cache = [[False for i in range(0, m + 1)] for j in range(0, n + 1)]
            function2(m - 1, n, cache)
        elapsed2 = (time.time() - start_time) * 1000.0 / 20

        values.append(avgSize)
        timeLine1.append(elapsed1)
        timeLine2.append(elapsed2)

    ##Generating the plot between time taken by each function call with n as variable and n

    plt.plot(values, timeLine1, 'r', label="Knapsack by Memoization")
    plt.plot(values, timeLine2, 'g', label="Knapsack by Dynamic Programming")
    plt.legend()
    plt.xlabel("Average size")
    plt.ylabel("Run Time in Milliseconds")
    plt.rcParams["figure.figsize"] = [16, 9]
    plt.show()

# def test_point_7():
#     global weights
#     for i in range(1, 11):
#         avgSize = 3000 * i
#         weights = weights_generator(800, avgSize)
#
#     n = 5000
#     weights
#     m = len(weights)
# print(knapsack_recursive(m - 1, n))
# #
# #
# # # Memoization params
# dp = [[False for i in range(0, m + 1)] for j in range(0, n + 1)]
# print(knapsack_memoization(m - 1, n, dp))
# #
# # # Dp
# print(knapsack_DP(m, n))

cache = []
showTime(knapsack_DP,knapsack_memoization,cache)
