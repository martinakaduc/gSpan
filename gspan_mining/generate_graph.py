import numpy as np

def check_size(graph):
    num_edge = (np.sum(graph > 0) - graph.shape[0]) / 2
    return num_edge

def generate(D, E, V, T, I, L):
    graphs = []
    subgraphs = []

    list_size_subgraph = np.random.poisson(lam=I, size=L)
    list_subgraph_probs = np.random.exponential(scale=1.0, size=L)
    list_subgraph_probs = list_subgraph_probs / sum(list_subgraph_probs)

    for sg_size in list_size_subgraph:
        num_node = np.random.randint(int(np.sqrt(sg_size)) + 1, sg_size + 2)
        list_node_label = np.random.randint(1, V + 1, num_node)
        list_edge_label = np.random.randint(1, E + 1, sg_size)

        subgraph = np.zeros((num_node, num_node))
        for i in range(subgraph.shape[0]):
            subgraph[i][i] = list_node_label[i]

        node_i = 0
        for i in range(sg_size):
            list_cand_edge_pos = np.where(subgraph[i] == 0)[0]
            node_j = np.random.choice(list_cand_edge_pos)

            subgraph[node_i][node_j] = list_edge_label[i]
            subgraph[node_j][node_i] = list_edge_label[i]

            node_i += 1
            if node_i >= num_node:
                node_i = 0

        subgraphs.append(subgraph)

    list_size_graph = np.random.poisson(lam=T, size=D)
    old_remaining_pattern = None

    for g_size in list_size_graph:
        graph = np.empty((0,), dtype=np.int32)

        if old_remaining_pattern is not None:
            pass

        current_graph_size = check_size(graph)
        while current_graph_size < g_size:
            tobe_add = np.random.choice(range(L), p=list_subgraph_probs)

            # Find Overlap
            subgraphs[tobe_add]

            if current_graph_size + list_size_subgraph[tobe_add] > g_size:
                pass
            else:
                pass

            current_graph_size = check_size(graph)

        graphs.append(graph)
