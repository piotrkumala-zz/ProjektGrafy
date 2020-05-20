import Shared.FlowNetwork

N=4
flow=Shared.FlowNetwork.FlowNetwork(N)
flow.addConnections(2*N)
flow.randomiseEdges(1,11)
print(flow)