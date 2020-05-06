from Shared.CoherentGraph import get_coherent_graph
from Shared.DistanceMatrix import distanceMatrix
from Shared.drawMatrix import drawMatrix



graph = get_coherent_graph(10, 0.5)
drawMatrix(distanceMatrix(graph))