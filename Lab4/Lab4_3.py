from Shared.connectedDirectedGraph import connectedDirectedGraph
from Shared.Canvas import draw_directed
from Shared.Bellman_ford import bellman_ford

graph=connectedDirectedGraph(10, 0.3)
graph.randomiseValues(-5, 10)
print(bellman_ford(graph,0))
draw_directed(graph)