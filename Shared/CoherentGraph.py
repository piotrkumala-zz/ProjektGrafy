from Shared.Graph import Graph
from Shared.Component import Components, is_one_coherent_component


def get_coherent_graph(n: int = 10, p: float = 0.5):
    i = 0
    while True:
        example_graph = Graph(n, p, 1)
        i += 1
        # if there's only one coherent component graph is coherent
        if is_one_coherent_component(Components(example_graph)):
            break
        if i > 10:
            print("Change graph parameters")
            break

    example_graph.add_weight_to_edges()
    return example_graph
