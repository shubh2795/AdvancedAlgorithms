import time
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sequences import *
import itertools

subst_matrix = {
    'A': {'A': 5, 'C': -1, 'G': -2, 'T': -1, '-': -3},
    'C': {'A': -1, 'C': 5, 'G': -3, 'T': -2, '-': -4},
    'G': {'A': -2, 'C': -3, 'G': 5, 'T': -2, '-': -2},
    'T': {'A': -1, 'C': -2, 'G': -2, 'T': 5, '-': -1},
    '-': {'A': -3, 'C': -4, 'G': -2, 'T': -1, '-': 0},
}


def match(n, m, A, B):
    # recursive function for match
    global subst_matrix
    sum = 0
    c = 5

    # one of the strings is empty
    if n == 0:
        for i in range(0, m):
            sum += subst_matrix['-'][B[i]]
        return sum

    if m == 0:
        for i in range(0, n):
            sum += subst_matrix[A[i]]['-']
        return sum

    l = subst_matrix[A[n - 1]]['-']
    r = subst_matrix['-'][B[m - 1]]

    if (A[n - 1] != B[m - 1]):
        c = subst_matrix[A[n - 1]][B[m - 1]]

    return max(match(n - 1, m, A, B) + l,  # delete from A
               match(n, m - 1, A, B) + r,  # delete from B
               match(n - 1, m - 1, A, B) + c)  # substitute


def matchDP(A, B):
    # DP code for match
    global subst_matrix
    n = len(A)
    m = len(B)
    cache = np.array([[0 for i in range(0, m + 1)] for j in range(0, n + 1)])
    sum = 0
    c = 5

    # fill in the base cases
    for j in range(1, m + 1):
        sum = sum + subst_matrix['-'][B[j - 1]]
        # print(i)
        cache[0][j] = sum
    sum = 0

    for i in range(1, n + 1):
        # print(j)
        sum = sum + subst_matrix[A[i - 1]]['-']
        cache[i][0] = sum

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = 5
            l = subst_matrix[A[i - 1]]['-']
            r = subst_matrix['-'][B[j - 1]]
            if (A[i - 1] != B[j - 1]):
                c = subst_matrix[A[i - 1]][B[j - 1]]  # update c if characters dont match.

            cache[i][j] = max(cache[i - 1][j] + l, cache[i][j - 1] + r, cache[i - 1][j - 1] + c)

        # uncomment this only to do traceback
        # if(cache[n][m] == 0):
        #     print("no output")
        # else:
    x = tracebackIter(n, m, A, B, cache)
    f = open("output.txt", "w")
    for i in range(len(x)):
        f.write(x[i] + "\n")
        f.write("score, " + str(cache[n][m]))
        f.close()

    return cache[n][m]


def traceback(n, m, A, B, cache):
    # recursive traceback
    global subst_matrix
    c = 5
    if n == 0 and m == 0:
        return []

    if n == 0:
        for j in range(m - 1, -1, -1):
            print("%s - %s" % ('_', B[j]))
        return

    if m == 0:
        for i in range(n - 1, -1, -1):
            print("%s - %s" % (A[i], '_'))
        return

    l = subst_matrix[A[n - 1]]['-']
    r = subst_matrix['-'][B[m - 1]]
    if (cache[n][m] == cache[n - 1][m] + l):
        print("%s - %s" % (A[n - 1], '_'))
        return traceback(n - 1, m, A, B, cache)

    if (cache[n][m] == cache[n][m - 1] + r):
        print("%s - %s" % ('_', B[m - 1]))
        return traceback(n, m - 1, A, B, cache)
    if (A[n - 1] != B[m - 1]):
        c = subst_matrix[A[n - 1]][B[m - 1]]
    if (cache[n][m] == cache[n - 1][m - 1] + c):
        print("%s - %s" % (A[n - 1], B[m - 1]))
        return traceback(n - 1, m - 1, A, B, cache)


def tracebackIter(n, m, A, B, cache):
    # iterative traceback
    global subst_matrix
    a1 = []
    i = m
    j = n
    c = 5

    while True:
        if (i == 0 and j == 0):
            break
        l = subst_matrix[A[j - 1]]['-']
        r = subst_matrix['-'][B[i - 1]]
        if (A[j - 1] == B[i - 1]):
            a1.append("%s - %s" % (A[j - 1], B[i - 1]))
            i = i - 1
            j = j - 1
        if (cache[j][i] == cache[j - 1][i] + l):
            a1.append("%s - %s" % (A[j - 1], '_'))
            j = j - 1
        if (cache[j][i] == cache[j][i - 1] + r):
            a1.append("%s - %s" % ('_', B[i - 1]))
            i = i - 1
        if (A[j - 1] != B[i - 1]):
            c = subst_matrix[A[j - 1]][B[i - 1]]
        if (cache[j][i] == cache[j - 1][i - 1] + c):
            a1.append("%s - %s" % (A[j - 1], B[i - 1]))
            i = i - 1
            j = j - 1
    return a1


# code for trying timing function.
def genStr(n):
    return (sequence1[1:n + 1], sequence2[1:n + 1])


def generateProblems(start, end, increment):
    # generates problems described as (size, (randstring, randstring))
    a = [(i, genStr(i)) for i in range(start, end, increment)]
    return a


def timeProblems(problemList, function, init=None, fit='exponential'):
    # Calculates the time taken by each function call and generates graph
    timeLine = []
    values = []
    for (size, args) in problemList:
        start_time = time.time()
        function(*args)  # use the * to unpack the tuple into arguments to the function
        elapsed = (time.time() - start_time) * 1000.0
        if elapsed > 0.0:
            timeLine.append(elapsed)
            values.append(size)

    plt.plot(values, timeLine, 'g')
    plt.xlabel("Problem size")
    plt.yscale('log')
    if fit == 'polynomial':
        plt.xscale('log')
    plt.ylabel("time in milliseconds")
    plt.rcParams["figure.figsize"] = [16, 9]
    plt.show()
    if fit == 'exponential':  # fit a straight line to n and log time
        slope, intercept, _, _, _ = stats.linregress([values], [np.log(t) for t in timeLine])
        print("time = %.6f %.3f ^ n" % (np.exp(intercept), np.exp(slope)))
    elif fit == 'polynomial':  # fit a straight line to log n and log time
        slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in values], [np.log(t) for t in timeLine])
        print("time = %.6f n ^ %.3f" % (np.exp(intercept), slope))
    plt.savefig('graph_Final.png')


# code to match first 5 sequences amongst themselves.
def findsubsets(s, n):
    return list(itertools.combinations(s, n))


def getScore():
    s = {sequence1[0:5001], sequence2[0:5001], sequence3[0:5001], sequence4[0:5001], sequence5[0:5001]}
    n = 2
    sequence_subset = findsubsets(s, n)
    for i in range(len(sequence_subset)):
        strs = sequence_subset[i]
        print(strs)
        print(matchDP(strs[0], strs[1]))
        print("\n")


# match a sequence with itself.
def getScoreWithItself():
    # find score of a sequence with itself.
    print(matchDP(sequence1, sequence1))
    print(matchDP(sequence2, sequence2))
    print(matchDP(sequence3, sequence3))
    print(matchDP(sequence4, sequence4))
    print(matchDP(sequence5, sequence5))


# timeProblems(generateProblems(1,10000,100), matchDP, fit = 'polynomial')
# getScore()
# getScoreWithItself()
# matchDP(sequence1[0:10001],sequence2[0:10001])
matchDP(sequence1[0:101], sequence2[0:101])
