import Shared.Graph
import Shared.CheckSeries
import Lab2.Lab2_2
import Shared.Component
import random
import copy

def generateEuler(n:int):
    while True:
        levels = [random.randrange(0,n,2) for _ in n]
        if Shared.CheckSeries(levels):
            break
        graph = Lab2.Lab2_2.createGraph(levels)
    while True:
        graph=Lab2.Lab2_2.randomize(graph,n/2)
        comp = Shared.Component.Components(graph)
        if (sum(comp)==len(comp)):
            break
    return graph

def EulerRec(graph: Shared.Graph.Graph, v:int):
    toReturn =f'{v}, '
    for i in graph.adjMatrix[v]:
        if i==1:
            graph.adjMatrix[v][i]=0
            graph.adjMatrix[i][v]=0
            toReturn+=EulerRec(graph,i)
    return toReturn

def findEuler(graph):
    Euler=""
    eulerGraph=copy.deepcopy(graph)
    return (EulerRec(eulerGraph,0))



