from Shared.DirectedGraph import DirectedGraph
from Shared.Kosaraju import kosaraju

g = DirectedGraph(5, 0.5)
g.print_list()

result = kosaraju(g)
all_paths = []

for i in set(result):
    all_paths.append([index for index, value in enumerate(result) if value == i])

for i in range(len(all_paths)):
    print(f"Sciezka {i + 1}: {all_paths[i]}")

