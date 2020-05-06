from Shared.Graph import Graph
from Shared.Converter import adj_to_list


def get_neighbours(graph: Graph, node_id: int):
    all_neighbours_list = adj_to_list(graph.adjMatrix)
    node_neighbours_list = all_neighbours_list[node_id]
    node_neighbours_list = list(map(lambda x: x - 1, node_neighbours_list))
    return node_neighbours_list


def get_edge_weight(graph: Graph, node_start: int, node_end: int):
    for edge in graph.edges:
        if edge.start == node_start and edge.end == node_end:
            return edge.weight
        if edge.start == node_end and edge.end == node_start:
            return edge.weight


def dijkstra(graph: Graph, start: int, end: int):
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
            sum_weight += get_edge_weight(graph, current, dist)
        current = dist

    path = path[::-1]
    return path, sum_weight
