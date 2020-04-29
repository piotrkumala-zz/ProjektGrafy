from Shared.Graph import Graph
from Shared.EdgeRandomization import randomize
from Shared.Generator import GenerateGraph

example_graph = Graph(5, 0.5, 1)
series = [7, 5, 5, 5, 3, 3, 2, 1, 1, 0]
output = GenerateGraph(series, len(series))
example_graph.change_adj_matrix(output.adjMatrix)

example_graph.printAdjacencyMatrix()
print("\n")

randomize(example_graph, 10)
example_graph.printAdjacencyMatrix()
