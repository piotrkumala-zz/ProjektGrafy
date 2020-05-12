from Shared.DirectedGraph import DirectedGraph

g = DirectedGraph(9, 0.5)
print('Adjacency list:')
g.print_list()
print('Adjacency matrix:')
g.print_adjacency_matrix()
print('Incidence matrix:')
g.print_incidence_matrix()