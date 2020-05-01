from Shared.CoherentGraph import get_coherent_graph
from Shared.Canvas import draw_graph

nodes = 5
probability = 0.5
example_graph = get_coherent_graph(nodes, probability)

for edge in example_graph.edges:
    print(edge)

draw_graph(example_graph)
