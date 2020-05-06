from Shared.Dijkstra import dijkstra


def distanceMatrix(graph):
    DistanceMatrix = [[dijkstra(graph, i,j)[1] for j in  range(graph.level())] for i in range(graph.level())]
    return DistanceMatrix


def findCentre(graph):
    dist=distanceMatrix(graph)
    sums = map(sum,dist)
    sums = list(sums)
    print(sums)
    return sums.index(min(sums))

def findMiniMax(graph):
    dist = distanceMatrix(graph)
    maxy = list(map(max, dist))
    print (maxy)
    return maxy.index(min(maxy))