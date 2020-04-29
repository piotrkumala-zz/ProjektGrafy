from Shared.Graph import Graph
import random


class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __hash__(self):
        return hash((self.start, self.end))

    def __eq__(self, other):
        return (self.start, self.end) == (other.start, other.end)


def randomize(graph: Graph, n: int):
    edges = []

    # check if edge
    for i in range(len(graph.adjMatrix)):
        for j in range(i):
            if graph.adjMatrix[i][j] == 1:
                edge = Edge(i, j)
                edges.append(edge)

    # ab, cd -> ad, cb
    i = 0
    while i < n:
        x, y = random.randint(0, len(edges) - 1), random.randint(0, len(edges) - 1)
        nodes = [edges[x].start, edges[x].end, edges[y].start, edges[y].end]
        if len(nodes) == len(set(nodes)):
            edges[x].end, edges[y].end = edges[y].end, edges[x].end
            i += 1

    # change adjMatrix
    for i in range(len(graph.adjMatrix)):
        for j in range(len(graph.adjMatrix)):
            graph.adjMatrix[i][j] = 0

    for val in edges:
        start = val.start
        end = val.end
        graph.adjMatrix[start][end] = 1
        graph.adjMatrix[end][start] = 1

