import Shared.Converter

graphAdj = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0], ]
graphInc = Shared.Converter.adj_to_inc(graphAdj)
graphList = [[3,4,7],[3,8],[1,2],[1,5,6],[4,7],[4,8],[1,5],[2,6]]



print(f'Adjacency to Incidence and List:')
print('Adjacency matrix:')
Shared.Converter.draw_matrix(graphAdj)
print('Incidence  matrix:')
Shared.Converter.draw_matrix(graphInc)
print('Adjacency list:')
Shared.Converter.draw_list(graphList)



graphAdj = Shared.Converter.inc_to_adj(graphInc)
graphList = Shared.Converter.inc_to_list(graphInc)

print(f'Incidence to Adjacency and List:')
print('Adjacency matrix:')
Shared.Converter.draw_matrix(graphAdj)
print('Incidence matrix:')
Shared.Converter.draw_matrix(graphInc)
print('Adjacency  list:')
Shared.Converter.draw_list(graphList)
graphList = [[3,4,7],[3,8],[1,2],[1,5,6],[4,7],[4,8],[1,5],[2,6]]
graphAdj = Shared.Converter.list_to_adj(graphList)
graphInc = Shared.Converter.list_to_inc(graphList)

print(f'List to Adjacency and Incidence:')
print('Adjacency  matrix:')
Shared.Converter.draw_matrix(graphAdj)
print('Incidence matrix:')
Shared.Converter.draw_matrix(graphInc)
print('Adjacency  list:')
Shared.Converter.draw_list(graphList)