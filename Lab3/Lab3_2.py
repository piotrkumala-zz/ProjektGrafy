from Shared.CoherentGraph import get_coherent_graph
from Shared.Canvas import draw_graph
from Shared.Dijkstra import dijkstra

nodes = 10
probability = 0.25
example_graph = get_coherent_graph(nodes, probability)

for edge in example_graph.edges:
    print(edge)
print("\n")

start_node = 0

for node in range(0, nodes):
    if node != start_node:
        path, weight = dijkstra(example_graph, start_node, node)

        print(f"Path from {start_node} to {node}: {path}, Sum of distances between vertices: {weight}")

draw_graph(example_graph)
