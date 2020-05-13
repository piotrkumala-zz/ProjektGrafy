from Shared.DirectedGraph import DirectedGraph
from Shared.Kosaraju import kosaraju


def connectedDirectedGraph(edges:int,prob:float):
    skladowe=[2]
    graph=None
    while max(skladowe)>1:
        graph=DirectedGraph(edges,prob)
        skladowe = kosaraju(graph)
    return graph