import Shared.Graph
import Shared.Component
import random
import copy
from Shared.Generator import GenerateGraph

def generateEuler(n:int):
    graph=False
    while True:
        levels = [random.randrange(0,n,2) for _ in range(n)]
        graph = GenerateGraph(levels, n)
        if graph is not False:
            comp = Shared.Component.Components(graph)
            if (sum(comp)==len(comp)):
                break

    return graph

def EulerRec(graph: Shared.Graph.Graph, v:int):
    toReturn =f'{v+1}, '
    for i in range(len(graph.adjMatrix)):
        if graph.adjMatrix[v][i]==1 and checkComponent(graph,v,i):
            graph.adjMatrix[v][i]=0
            graph.adjMatrix[i][v]=0
            toReturn+=EulerRec(graph,i)
            break
    else:
        for i in range(len(graph.adjMatrix)):
            if graph.adjMatrix[v][i] == 1:
                graph.adjMatrix[v][i] = 0
                graph.adjMatrix[i][v] = 0
                toReturn += EulerRec(graph, i)
                break
    return toReturn

def findEuler(graph):
    eulerGraph=copy.deepcopy(graph)
    return (EulerRec(eulerGraph,0))

def checkComponent(graph,v,i):
    n = sum(Shared.Component.Components(graph))
    graph.adjMatrix[v][i] = 0
    graph.adjMatrix[i][v] = 0
    m = sum(Shared.Component.Components(graph))
    graph.adjMatrix[v][i] = 1
    graph.adjMatrix[i][v] = 1
    if n==m:
        return True
    return False

