import random


class Node:

    counter = 0

    def __init__(self):
        self.edges = []
        self.number = self.counter
        Node.counter+=1

    def add_edge(self, Edge):
        self.edges.append(Edge)


    def isNeighboor(self,node):
        for edge in self.edges:
            if edge.dest == node:
                return True
        return False
    def __len__(self):
        return len(self.edges)

class Edge:
    def __init__(self, src: Node, dest: Node, value: int = 0):
        self.src = src
        self.dest = dest
        self.value = value
        src.add_edge(self)
        dest.add_edge(self)
    def __str__(self):
        return 'dest: ' + str(self.dest.number) + ' val: ' + str(self.value)


class Layer:
    counter=0
    def __init__(self,N :int,):
        self.Nodes = [Node() for _ in range(N)]
        self.FullyConnected = False
        self.number=self.counter
        Layer.counter+=1

    def checkIfConnected(self):
        suma=sum(list(map(len,self.Nodes)))
        if suma>=len(self.Nodes):
            self.FullyConnected=True

    def connect(self,other: 'Layer'):
        for node in self.Nodes:
            rand=random.randrange(len(other))
            while len(other.Nodes[rand].edges)!=0 and other.FullyConnected is False:
                rand = random.randrange(len(other))
            Edge(node, other.Nodes[rand])
            other.checkIfConnected()
        if other.FullyConnected is False:
            for node in other.Nodes:
                if len(node.edges) == 0:
                    rand = random.randrange(len(self))
                    while self.Nodes[rand].isNeighboor(node):
                        rand = random.randrange(len(self))
                    node.add_edge(Edge(self.Nodes[rand],node))
    def __len__(self):
        return len(self.Nodes)

class FlowNetwork:

    def __init__(self,N:int):
        if N<2:
            raise Exception("Not enought layers of network")
        else:
            self.Layers = []
            self.Layers.append(Layer(1))
            for i in range(1,N+1):
                rand=random.randrange(2,N)
                self.Layers.append(Layer(rand))
                self.Layers[i-1].connect(self.Layers[i])
            self.Layers.append(Layer(1))
            self.Layers[N].connect(self.Layers[N+1])


    def addConnections(self,N:int):
        allNodes=[]
        for i in range(len(self.Layers)):
            allNodes+=self.Layers[i].Nodes
        for i in range(N-1):
            rand=random.randrange(len(allNodes)-1)
            rand2=random.randrange(1,len(allNodes))
            while allNodes[rand].isNeighboor(allNodes[rand2]):
                rand = random.randrange(len(allNodes))
                rand2 = random.randrange(len(allNodes))
            Edge(allNodes[rand],allNodes[rand2])

    def randomiseEdges(self,rangedown,rangeup):
        allEdges=[]
        for i in self.Layers:
            for j in i.Nodes:
                allEdges+=j.edges
        for edge in allEdges:
            edge.value=random.randrange(rangedown,rangeup)

    def __str__(self):
        query='Layers:\n'
        for i in self.Layers:
            query+=str(i.number)+'. :\t'
            for j in i.Nodes:
                query+=str(j.number)+', '
            query+='\n'
        query+='Edges:\n'
        allNodes = []
        for i in range(len(self.Layers)):
            allNodes += self.Layers[i].Nodes
        for i in allNodes:
            query+=str(i.number)+'. :\t'
            for j in i.edges:
                if j.src==i:
                    query+=str(j)+' | '
            query+='\n'
        return query
