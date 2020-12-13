N = 5
def lowestCost(graph, goalV):
    bestCost = {}
    heap = Heap(N)
    for i in range(N):
        heap.push(i, float('inf'))
        bestCost[i] = float('inf')
    heap.promote(goalV, 0)
    bestCost[goalV] = 0

    while not heap.empty():
        v = heap.pop()
        for i in range(v):
            newCost = bestCost[v] + graph[v, i]
            if newCost < bestCost[i]:  # if updated, then promote the vertex in the min-heap
                bestCost[i] = newCost
                heap.promote(i, newCost)

    return bestCost

