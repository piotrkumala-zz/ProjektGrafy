from Shared.connectedDirectedGraph import connectedDirectedGraph
from Shared.Canvas import draw_directed
from Shared.Johnson import johnson
from Shared.drawMatrix import drawMatrix

graph=connectedDirectedGraph(3, 0.5)
graph.randomiseValues(-2, 10)
drawMatrix(graph.Values)
print(johnson(graph))
draw_directed(graph)