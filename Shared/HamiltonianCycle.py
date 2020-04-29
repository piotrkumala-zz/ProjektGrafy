def is_hamiltonian_cycle(graph, path, pos):
    if pos == len(graph.adjMatrix):
        if graph.adjMatrix[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(1, len(graph.adjMatrix)):
        if graph.adjMatrix[path[pos - 1]][v] == 1 and v not in path:
            path.append(v)
            if is_hamiltonian_cycle(graph, path, pos + 1):
                return True
            path.pop()
    return False


def print_hamiltonian_cycle(path):
    for node in path:
        print(node, end="-")
    print(path[0])


def hamiltonian_cycle(graph):
    path = [0]
    if is_hamiltonian_cycle(graph, path, 1):
        print_hamiltonian_cycle(path)
    else:
        print("Hamiltonian cycle does not exist\n")
