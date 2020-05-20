from Shared.DirectedGraph import DirectedGraph
from Shared.Kosaraju import kosaraju
from Shared.Canvas import draw_directed
g = DirectedGraph(10, 0.2)
g.print_list()

result = kosaraju(g)
all_paths = []

for i in set(result):
    all_paths.append([index for index, value in enumerate(result) if value == i])

for i in range(len(all_paths)):
    print(f"Składowa {i + 1}: {all_paths[i]}")

draw_directed(g)