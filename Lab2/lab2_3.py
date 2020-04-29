import Shared.Graph
from Shared.Component import Components
import Shared.Canvas as Canvas

graph=Shared.Graph.Graph(10,0.1,1)
comp=Components(graph)
Shared.Component.printComponent(comp)
Canvas.draw_graph(graph)