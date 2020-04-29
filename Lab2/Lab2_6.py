from Shared.Graph import Graph
from Shared.Canvas import draw_graph
from Shared.HamiltonianCycle import hamiltonian_cycle


example_graph = Graph(10, 0.5, 1)
hamiltonian_cycle(example_graph)
draw_graph(example_graph)
