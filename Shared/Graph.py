import random


class Graph(object):
    def __init__(self, vertexes: int, edges: int):
        """ Create a random graph with given params and print it's adjacency matrix
        :param vertexes: number of vertexes in graph
        :param edges: number of edges in graph
        """
        self.adjMatrix = []
        for i in range(vertexes):
            self.adjMatrix.append([0 for i in range(vertexes)])
        self.size = vertexes
        v1 = 0
        v2 = 0
        for i in range(edges):
            v1 = random.randint(0, vertexes - 1)
            v2 = random.randint(0, vertexes - 1)
            while v1 == v2:
                v2 = random.randint(0, vertexes - 1)
            self.addEdge(v1, v2)
        self.printAdjacencyMatrix()

    # noinspection PyRedeclaration
    def __init__(self, vertexes: int, probability: float):
        """Create a random graph with given params and print it's adjacency matrix
        :param vertexes: number of vertexes in graph
        :param probability:  probability that two vertexes are connected
        """
        self.adjMatrix = []
        for i in range(vertexes):
            self.adjMatrix.append([0 for i in range(vertexes)])
        self.size = vertexes
        for v1 in range(vertexes):
            for v2 in range(vertexes):
                if v1 == v2:
                    continue
                elif random.random() < probability:
                    self.addEdge(v1, v2)
                else:
                    continue
        self.printAdjacencyMatrix()

    def addEdge(self, v1, v2):
        """Create an edge between graph's two vertexes
        :param v1: first vertex
        :param v2: second vertex
        :return: nothing
        """
        if v1 == v2:
            print("Already exists")
            return
        if v1 > self.size - 1 or v2 > self.size - 1:
            print("Size of the graph exceeded")
            return
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        """ Removes edge between two vertexes
        :param v1: first vertex
        :param v2: second vertex
        :return:
        """
        if self.adjMatrix[v1][v2] == 0:
            print("Nothing to delete")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        """ Checks if graph contains an edge between two vertexes
        :param v1: first vertex
        :param v2: second vertex
        :return: boolean
        """
        return True if self.adjMatrix[v1][v2] > 0 else False

    def printAdjacencyMatrix(self):
        """ Prints graph's adjacency matrix
        """
        for row in self.adjMatrix:
            for val in row:
                print("%d " % val, end='')
            print("")
