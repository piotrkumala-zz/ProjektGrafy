from Shared.DirectedGraph import DirectedGraph


def kosaraju(graph: DirectedGraph):
    d = [-1 for _ in range(graph.size)]
    f = [-1 for _ in range(graph.size)]

    t = [0]
    for v in range(graph.size):
        if d[v] == -1:
            dfs_visit(v, graph, d, f, t)

    nr = 0
    transposed_graph = transpose_graph(graph)
    comp = [-1 for _ in range(graph.size)]

    for v in reversed(sorted(range(len(f)), key=lambda key: f[key])):
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_r(nr, v, transposed_graph, comp)
    return comp


def dfs_visit(v: int, graph: DirectedGraph, d: list, f: list, t: list):
    t[0] += 1
    d[v] = t[0]
    for u in graph.get_neighbours(v):
        if d[u] == -1:
            dfs_visit(u, graph, d, f, t)
    t[0] += 1
    f[v] = t[0]


def components_r(nr: int, v: int, transposed_graph: list, comp: list):
    for u in transposed_graph[v]:
        if comp[u] == -1:
            comp[u] = nr
            components_r(nr, u, transposed_graph, comp)


def transpose_graph(graph: DirectedGraph):
    transposed_list = [[] for _ in range(graph.size)]
    for i in range(graph.size):
        for j in graph.list[i]:
            transposed_list[j].append(i)
    return transposed_list
