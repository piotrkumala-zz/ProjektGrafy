import math
from Shared.DirectedGraph import DirectedGraph


def bellman_ford(graph: DirectedGraph,start:int):
    d=[math.inf for _ in range(graph.level())]
    p=[None for _ in range(graph.level())]
    d[start]=0
    for _ in range(graph.level()):
        for i in range(graph.level()):
            for j in range(graph.level()):
                if graph.adjMatrix[i][j] != 0:
                    if d[j]>d[i]+graph.Values[i][j]:
                        d[j]=d[i]+graph.Values[i][j]
                        p[j]=i
    for i in range(graph.level()):
        for j in range(graph.level()):
            if graph.adjMatrix[i][j] != 0:
                if d[j]>d[i]+graph.Values[i][j]:
                    print("ujemny cykl wykryty")
                    return False
    return d, p