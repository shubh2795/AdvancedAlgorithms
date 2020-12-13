class Graph:

    def __init__(self, N, matrix, density=1.0, debug=False):
        self.size = N
        self.matrix = matrix
        self.density = density
        self.maxEdgeCost = 10000
        if matrix:
            self.graph = self._createGraph_Matrix(N, density, debug)
        else:
            self.graph = self._createGraph_List(N, density, debug)

    def getSize(self):
        return self.size

    def getEdges(self, nodeId):
        if self.matrix:
            return [(i, self.graph[nodeId, i]) for i in range(0, size)]
        return self.graph[nodeId]

    def _createGraph_Matrix(self, N, density, debug):
        g = np.random.random((N, N)) * self.maxEdgeCost

        for i in range(0, N):
            for j in range(0, N):
                g[i, j] = float('inf') if np.random.random_sample() >= density else g[i, j]
        # set self edge costs to 0
        for i in range(0, N):
            g[i, i] = 0
        if debug:  # graph with at least one low-cost path
            # build one bi-directional path through the graph
            for i in range(0, N):
                g[(i - 1) % N, i] = 1
        return g

    def _createGraph_List(self, N, density, debug):
        return self._convertToList(self._createGraph_Matrix(N, density, debug))

    def _convertToList(self, g):
        # returns a list of lists of the graph
        # let gL be this list,
        # then gL[i] represents the ith node
        # and is a list of the form [.... , (j, g[i,j]), .....]
        # each tuple is (node connectd to i, the cost from i to j )
        return [[(j, g[i, j]) for j in range(0, N) if g[i, j] != float("inf")] for i in range(0, N)]

# N = 10
# for debug in [True, False]:
#     for density in [0.0, 0.5, 1.0]:
#         print("\nDebug = %s Density = %5.3f **********************************************" % (str(debug), density))
#         # test matrix
#         graph_matrix = Graph(N, matrix = False, density = density, debug = debug)
#         for i in range(0, graph_matrix.getSize()):
#             print(graph_matrix.getEdges(i))
#         # test list
#         graph_list = Graph(N, matrix = False, density = density, debug = debug)
#         for i in range(0, graph_list.getSize()):
#             print(graph_list.getEdges(i))
