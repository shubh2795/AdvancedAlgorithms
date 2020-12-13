# Min heap, the keys of parent nodes are less than or equal to those of the 
# children and the lowest's key is in the root node
class Heap:
    # The init method or constructor  
    def __init__(self, howMany):
        self.maxSize = howMany  # maximum number of items that can be stored
        self.graphToHeap = {}  # maps a graph node index to its index in the heap
        self.heapToGraph = {}  # maps an index in the heap its graph node index
        self.lastIndex = -1  # index of the last item in the heap
        self.minCost = np.ones((self.maxSize)) * float('inf')  # allocate the memory

    # PUBLIC methods
    def empty(self):
        return self.lastIndex == -1

    def getMinCost(self, graphIndex):
        x = self.heapToGraph[graphIndex]
        return self.minCost[x]

    def push(self, graphIndex, value):
        # if self.lastIndex+1 >= self.maxSize:
        #     return

        self.lastIndex = self.lastIndex + 1
        self.minCost[self.lastIndex] = value
        self.graphToHeap[graphIndex] = self.lastIndex
        self.heapToGraph[self.lastIndex] = graphIndex

        current = self.lastIndex
        # heapify upwards
        while (current > 0 and self.minCost[current] < self.minCost[self._parent(current)]):
            self.swap(current, self._parent(current))
            current = self._parent(current)

    def pop(self):
        if not self.empty():
            popped = self.minCost[0]
            x = self.heapToGraph[0]
            self.minCost[0] = self.minCost[self.lastIndex]
            self.minCost[self.lastIndex] = float('inf')
            y = self.heapToGraph[self.lastIndex]
            self.heapToGraph[0] = y
            self.lastIndex = self.lastIndex - 1
            self.graphToHeap[y] = 0
            self.heapify(0)  # heapify down
            return (x, popped)

    def promote(self, graphIndex, newCost):
        self.minCost[self.graphToHeap[graphIndex]] = newCost
        # heapify from the parent or not
        self.heapify(self.graphToHeap[graphIndex])

    # heapify down
    def heapify(self, x):
        if not ((x >= ((self.lastIndex + 1) // 2) and x <= self.lastIndex + 1)):
            if (self.minCost[x] > self.minCost[self._leftC(x)] or self.minCost[x] > self.minCost[self._rightC(x)]):

                if self.minCost[self._leftC(x)] < self.minCost[self._rightC(x)]:
                    self.swap(x, self._leftC(x))
                    self.heapify(self._leftC(x))
                else:
                    self.swap(x, self._rightC(x))
                    self.heapify(self._rightC(x))

    def printHeap(self):
        # useful for debugging
        for i in range(0, self.maxSize // 2):
            if self._rightC(i) < self.maxSize:
                print("p = %5.3f l = %5.3f r = %5.3f" %
                      (self.minCost[i], self.minCost[self._leftC(i)], self.minCost[self._rightC(i)]))
            else:
                print("p = %5.3f l = %5.3f" %
                      (self.minCost[i], self.minCost[self._leftC(i)]))

    def _parent(self, index):
        return floor((index - 1) / 2)

    def _leftC(self, index):
        return 2 * index + 1

    def _rightC(self, index):
        return 2 * index + 2

    def swap(self, x, y):
        i = self.heapToGraph[x]
        j = self.heapToGraph[y]

        self.minCost[x], self.minCost[y] = self.minCost[y], self.minCost[x]

        self.graphToHeap[i] = y
        self.graphToHeap[j] = x

        self.heapToGraph[x] = j
        self.heapToGraph[y] = i


