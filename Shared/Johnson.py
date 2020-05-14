from Shared.DirectedGraph import DirectedGraph
import copy
from Shared.Bellman_ford import bellman_ford

def johnson(graph:DirectedGraph):
    newGraph=copy.deepcopy(graph)
    num=newGraph.add_verticle()
    for i in range(newGraph.level()-1):
        newGraph.add_edge(num,i)
    d,p=bellman_ford(newGraph,num)
    h=[None for _ in range(newGraph.level())]
    for i in range(newGraph.level()):
        h[i]=d[i]
    for i in range(graph.level()):
        for j in range(i,graph.level()):
            if graph.adjMatrix[i][j] != 0:
               graph.Values[i][j]+=h[j]-h[i]
    D=[[dijkstra(graph,i,j) -h[j]+h[i] for j in range(graph.level())]for i in range(graph.level())]
    return D




from Shared.Converter import adj_to_list


def get_neighbours(graph, node_id: int):
    node_neighbours_list=[]
    for i in range(graph.level()):
        if graph.adjMatrix[node_id][i]==1:
            node_neighbours_list.append(i)
    return node_neighbours_list


def get_edge_weight(graph, node_start: int, node_end: int):
    return graph.Values[node_start][node_end]


def dijkstra(graph, start: int, end: int):
    current = start
    visited = set()
    shortest_paths = {start: (None, 0)}
    sum_weight = 0

    while current != end:
        visited.add(current)
        destinations = get_neighbours(graph, current)
        current_edge_weight = shortest_paths[current][1]

        for dist in destinations:
            weight = get_edge_weight(graph, current, dist) + current_edge_weight
            if dist not in shortest_paths:
                shortest_paths[dist] = (current, weight)
            else:
                current_shortest_weight = shortest_paths[dist][1]
                if current_shortest_weight > weight:
                    shortest_paths[dist] = (current, weight)

        next_destinations = dict()
        for node in shortest_paths:
            if node not in visited:
                next_destinations[node] = shortest_paths[node]

        current = min(next_destinations, key=lambda key: next_destinations[key][1])

    path = []
    while current is not None:
        path.append(current)
        dist = shortest_paths[current][0]
        if dist is not None:
                sum_weight += get_edge_weight(graph, dist, current)
        current = dist

    path = path[::-1]
    return sum_weight