import numpy as np


def adj_to_inc(adj: list):
    edges = np.sum(adj)//2
    edges_counter = 0
    temp_inc = [[0 for _ in range(edges)] for _ in range(len(adj))]
    for x in range(len(adj)):
        for y in range(x,len(adj)):
            if edges_counter < int(edges):
                temp_inc[x][edges_counter] += adj[x][y]
                temp_inc[y][edges_counter] += adj[x][y]
                edges_counter += adj[x][y]
    return temp_inc


def adj_to_list(adj: list):
    temp_list = [[] for _ in range(len(adj))]
    for x in range(len(adj)):
        for y in range(x,len(adj)):
            if adj[x][y] == 1:
                temp_list[x].append(y+1)
                temp_list[y].append(x+1)
    return temp_list


def inc_to_adj(inc: list):
    nodes = len(inc)
    edges = len(inc[0])
    temp_adj = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for x in range(edges):
        z1 = -1
        z2 = -1
        for y in range(nodes):
            if inc[y][x] == 1:
                if z1 < 0:
                    z1 = y
                else:
                    z2 = y
                    temp_adj[z1][z2] = 1
                    temp_adj[z2][z1] = 1
                    break
    return temp_adj


def list_to_adj(lista: list):
    nodes=len(lista)
    temp_adj = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for x in range(nodes):
        for y in range(len(lista[x])):
            temp_adj[x][lista[x][y]-1]=1;
    return temp_adj


def list_to_inc(lista: list):
    temp = list_to_adj(lista)
    return adj_to_inc(temp)


def inc_to_list(inc: list):
    temp = inc_to_adj(inc)
    return adj_to_list(temp)


def draw_matrix(matrix: list):
    for row in matrix:
        for val in row:
            print('%d ' % val, end='')
        print('')


def draw_list(lista: list):
    for row in range(len(lista)):
        print(f'{row+1}:', end='')
        for val in lista[row]:
            print(f'{val} ', end='')
        print('')