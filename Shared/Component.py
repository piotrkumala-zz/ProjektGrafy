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
    printComponent(comp)
    return comp


def ComponentsR(i: int,nr: int,comp,graph: Shared.Graph.Graph):
    for j in range(graph.level()):
        if graph.checkNeighbors(i,j) and comp[j]==-1:
            comp[j]=nr
            ComponentsR(j,nr,comp,graph)
