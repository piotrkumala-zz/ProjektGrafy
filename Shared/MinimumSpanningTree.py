import random

from Shared.Edge import Edge
from Shared.Graph import Graph


def get_minimum_spanning_tree(start_graph: Graph):

    start = random.randint(0, start_graph.size)
    vertexes = list()
    vertexes.append(start)
    out = Graph(start_graph.size, 0, 1)
    potential_edges = list()
    while len(vertexes) < out.size:
        for edge in start_graph.edges:
            if len(out.edges) == 0 and (edge.start == start or edge.end == start):
                potential_edges.append(edge)
            for tree_edge in out.edges:
                if edge.start == tree_edge.start or edge.start == tree_edge.end or edge.end == tree_edge.start \
                        or edge.end == tree_edge.end:
                    potential_edges.append(edge)

        potential_edges = list(set(potential_edges))
        potential_edges.sort(key=lambda item: item.weight)

        out.edges.append(Edge(potential_edges[0].start, potential_edges[0].end, potential_edges[0].weight))
        out.values[potential_edges[0].start][potential_edges[0].end] = potential_edges[0].weight
        out.values[potential_edges[0].end][potential_edges[0].start] = potential_edges[0].weight
        out.addEdge(potential_edges[0].start, potential_edges[0].end)

        vertexes.append(potential_edges[0].start)
        vertexes.append(potential_edges[0].end)

        vertexes = list(set(vertexes))
        for edge in start_graph.edges:
            if edge.start in vertexes and edge.end in vertexes:
                start_graph.edges.remove(edge)
        potential_edges.clear()
    return out
