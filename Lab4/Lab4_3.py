from Shared.connectedDirectedGraph import connectedDirectedGraph
from Shared.Canvas import draw_directed
from Shared.Bellman_ford import bellman_ford
from Shared.drawMatrix import drawMatrix

graph=connectedDirectedGraph(10, 0.3)
graph.randomiseValues(-2, 10)
drawMatrix(graph.Values)
print(bellman_ford(graph,0))
draw_directed(graph)