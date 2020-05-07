import random

from Shared.Canvas import draw_graph
from Shared.CoherentGraph import get_coherent_graph
from Shared.MinimumSpanningTree import get_minimum_spanning_tree

nodes = 10
probability = 0.5
start_graph = get_coherent_graph(nodes, probability)

out = get_minimum_spanning_tree(start_graph, nodes)

for edge in out.edges:
    print(edge)

draw_graph(out)
