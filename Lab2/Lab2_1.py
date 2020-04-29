from Shared.CheckSeries import CheckSeries
from Shared.Converter import adj_to_list
from Shared.Generator import GenerateGraph

series = [7, 7, 5, 5, 3, 3, 1, 1]
print(series)
print(CheckSeries(series[:], 8))
#output = GenerateGraph(series, 8)
#print(adj_to_list(output.adjMatrix))
series = [7, 5, 5, 5, 3, 3, 2, 1, 1, 0]
print(series)
print(CheckSeries(series, 10))
series = [3, 3, 2, 2]
print(series)
print(CheckSeries(series[:], 4))
output = GenerateGraph(series, 4)
print(adj_to_list(output.adjMatrix))