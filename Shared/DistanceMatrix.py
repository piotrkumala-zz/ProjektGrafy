


def DistanceMatrix(graph):
    DistanceMatrix = [djikstra(graph, i) for i in range(graph.level())]
    return DistanceMatrix