from Shared.connectedDirectedGraph import connectedDirectedGraph
from Shared.Canvas import draw_directed
from Shared.Johnson import johnson
from Shared.drawMatrix import drawMatrix

graph=connectedDirectedGraph(10, 0.3)
graph.randomiseValues(-2, 10)
drawMatrix(graph.Values)
print(drawMatrix(johnson(graph)))
draw_directed(graph)