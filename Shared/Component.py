import  Shared.Graph


def printComponent(comp):
    for i in range(1,len(comp)):
        verticles=''
        for j in range(len(comp)):
            if comp[j] == i:
                verticles+=f"{j+1}, "
        if verticles != '':
            print (f"{i}: {verticles}")

def Components(graph: Shared.Graph.Graph):
    comp=[-1 for _ in range(graph.level())]
    nr=0
    for i in range(graph.level()):
        if comp[i]==-1:
            nr+=1
            comp[i]=nr
            ComponentsR(i,nr,comp,graph)
    return comp


def ComponentsR(i: int,nr: int,comp,graph: Shared.Graph.Graph):
    for j in range(graph.level()):
        if graph.checkNeighbors(i,j) and comp[j]==-1:
            comp[j]=nr
            ComponentsR(j,nr,comp,graph)


def is_one_coherent_component(comp):
    num_pow = 0
    for i in range(1, len(comp)):
        vertices = 0
        for j in range(len(comp)):
            if comp[j] == i:
                vertices += 1
        if vertices != 0:
            num_pow += 1
    if num_pow == 1:
        return True
    return False
