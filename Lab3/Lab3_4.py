from Shared.DistanceMatrix import distanceMatrix,findCentre,findMiniMax
from Shared.CoherentGraph import get_coherent_graph
from Shared.Canvas import draw_graph
from Shared.drawMatrix import drawMatrix

graph = get_coherent_graph(10, 0.5)
distanceMatrix=distanceMatrix(graph)
print("Macierz odległości:")
drawMatrix(distanceMatrix)
centrum=findCentre(graph)
miniMax=findMiniMax(graph)
print("")
print(f"centrum:{centrum+1}")
print(f"miniMax:{miniMax+1}")



