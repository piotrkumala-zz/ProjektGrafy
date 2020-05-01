from Shared.Graph import Graph
from Shared.Edge import Edge
import random


def randomize(graph: Graph, n: int = 1):
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
        edge_1 = Edge(edges[x].start, edges[y].end)
        edge_2 = Edge(edges[y].start, edges[x].end)
        if edge_1 not in edges and edge_2 not in edges and len(nodes) == len(set(nodes)):
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
