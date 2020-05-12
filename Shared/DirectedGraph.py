import random


class DirectedGraph:
    def __init__(self, vertexes: int, probability: float):
        self.adjMatrix = []
        self.list = []
        self.incMatrix = []
        self.size = vertexes
        for i in range(vertexes):
            self.adjMatrix.append([0 for i in range(vertexes)])
            self.list.append([])
            self.incMatrix.append([])
        for i in range(vertexes):
            for j in range(vertexes):
                if i == j:
                    continue
                if random.random() < probability:
                    self.add_edge(i, j)

    def add_edge(self, v1: int, v2: int):
        self.adjMatrix[v1][v2] = 1
        self.list[v1].append(v2)
        new_column = [0 for i in range(self.size)]
        new_column[v1] = 1
        new_column[v2] = -1
        for i in range(self.size):
            self.incMatrix[i].append(new_column[i])

    def print_list(self):
        for i in range(self.size):
            print('%d: ' % i, end='')
            for j in self.list[i]:
                print('%d '% j, end='')
            print()

    def print_adjacency_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print("%d " % val, end='')
            print("")

    def print_incidence_matrix(self):
        for row in self.incMatrix:
            for val in row:
                if val >= 0:
                    print(" %d " % val, end='')
                else:
                    print("%d " % val, end='')
            print("")
