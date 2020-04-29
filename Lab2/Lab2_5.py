from Shared.Converter import adj_to_list
from Shared.EdgeRandomization import randomize
from Shared.Generator import GenerateKGraph

g  = GenerateKGraph(7, 2)
print(adj_to_list(g.adjMatrix))
print("\n")
randomize(g, 100)
print(adj_to_list(g.adjMatrix))

