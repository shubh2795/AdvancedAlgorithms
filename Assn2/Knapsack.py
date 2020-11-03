from stop_watch import start_watch, stop_watch_print


def knapsack(n, m, weights):
    if n == 0:
        return 0
    if m == -1:
        return 0
    if weights[m] <= n:
        return max(weights[m] + knapsack(n - weights[m], m - 1, weights),
                   knapsack(n, m - 1, weights))
    else:
        return knapsack(n, m - 1, weights)


def knapsack_memo(n, m, weights, dp):
    if n == 0 or m == -1: return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if weights[m] <= n:
        res = max(weights[m] + knapsack_memo(n - weights[m], m - 1, weights, dp),
                  knapsack_memo(n, m - 1, weights, dp))
        dp[n][m] = res
        return res
    else:
        res = knapsack_memo(n, m - 1, weights, dp)
        dp[n][m] = res
        return res


def knapsack_DP(m,n, weights):
    dp = [[0 for i in range(0, m + 1)] for j in range(0, n + 1)]
    dp[n][0] = 0
    for i in range(1, m + 1):
        for j in range(0, n + 1):
            if weights[i - 1] <= j:
                dp[j][i] = max(dp[j][i - 1], dp[j - weights[i - 1]][i - 1] + weights[i - 1])
            else:
                dp[j][i] = dp[j][i - 1]
    return dp[n][m]


def knapsack_DP_reconstruct(W, weights):
    dp = [[0 for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
    n = len(weights)
    decisions = [[False for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
    dp[W][0] = 0
    for i in range(1, n + 1):
        for w in range(0, W + 1):
            if weights[i - 1] <= w:
                if dp[w - weights[i - 1]][i - 1] + weights[i - 1] > dp[w][i - 1]:
                    # We record the decision here that its beneficial to pick the ith item
                    decisions[w][i] = True
                    dp[w][i] = dp[w - weights[i - 1]][i - 1] + weights[i - 1]
                else:
                    dp[w][i] = dp[w][i - 1]
            else:
                dp[w][i] = dp[w][i - 1]

    i = n
    w = W
    while i > 0 and w > 0:
        if decisions[w][i]:
            print("Picked up {} , Weight {}".format(i - 1, weights[i - 1]))
            w -= weights[i - 1]
            i -= 1;
        else:
            i -= 1
    return dp[W][n]


weights = [3, 6, 10, 6]

W = 20
N = len(weights)
# Recursive solution
start_watch()
print(knapsack(W, N - 1, weights))
stop_watch_print("Recursive solution {} millis")

# Memoization
dp = [[-1 for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
start_watch()
print(knapsack_memo(W, N - 1, weights, dp))
stop_watch_print("Memoization solution {} millis") \
 \
# Bottom up
start_watch()
print(knapsack_DP(W, weights))
stop_watch_print("Bottom up solution {} millis")

# Bottom up with solution reconstruction
print(knapsack_DP_reconstruct(W, weights))
