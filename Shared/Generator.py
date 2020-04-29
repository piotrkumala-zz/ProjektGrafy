from Shared.CheckSeries import CheckSeries
from Shared.Graph import Graph


def GenerateGraph(a: [], n: int):
    if CheckSeries(a[:], n):
        a.sort(reverse=True)
        b = list(range(0, n))
        g = Graph(n, 0.0, 1)
        while True:
            empty = True
            negative = False
            for x in a:
                if x != 0:
                    empty = False
                if x < 0:
                    negative = True
            if empty:
                return g
            elif a[0] < 0 or a[0] >= n or negative:
                return False
            else:
                i = 1
                while i <= a[0]:
                    a[i] -= 1
                    g.addEdge(b[0], b[i])
                    i += 1
                a[0] = 0
                for i in range(n - 1):
                    for j in range(n - 1):
                        if a[j] < a[j + 1]:
                            a[j], a[j + 1] = a[j + 1], a[j]
                            b[j], b[j + 1] = b[j + 1], b[j]
    else:
        return False
def GenerateKGraph(n:int, k:int):
    a = list()
    for i in range(n):
        a.append(k)
    return GenerateGraph(a,n)