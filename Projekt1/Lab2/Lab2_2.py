from Shared.Graph import Graph
import random

example_graph = Graph(6, 0.25)


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
    for i in range(len(graph.adjMatrix)):
        for j in range(i):
            if graph.adjMatrix[i][j] == 1:
                xx = Edge(i, j)
                edges.append(xx)

    # ab, cd -> ad, cb
    for i in range(n):
        x, y = random.randint(0, len(edges) - 1), random.randint(0, len(edges) - 1)
        a = edges[x].start
        b = edges[x].end
        c = edges[y].start
        d = edges[y].end
        edges[x].end = d
        edges[y].end = b

    for i in range(len(graph.adjMatrix)):
        for j in range(len(graph.adjMatrix)):
            graph.adjMatrix[i][j] = 0

    for val in edges:
        start = val.start
        end = val.end
        if start != end:
            graph.adjMatrix[start][end] = 1
            graph.adjMatrix[end][start] = 1


randomize(example_graph, 1)
print(example_graph.adjMatrix)
