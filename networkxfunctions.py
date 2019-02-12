import networkx as nx
import math

def get_graph_from_file(file_path):
    edges = []
    with open(file_path, 'r') as f:
        for line in f:
            if not line[0] == '%' and not line[1] == '#':
                parts = line.split()
                edges.append((parts[0], parts[1]))
    graph = nx.Graph()
    graph.add_edges_from(edges)
    return graph

def get_fi(graph, n_id):
    return  sum([graph.degree(n1) for n1 in graph.neighbors(n_id)])/graph.degree(n_id)**2

def get_node_dict(graph, n_id):
    n_dict =  {
            'id': n_id,
            'degree': graph.degree(n_id),
            'fi': get_fi(graph, n_id)
        }
    return n_dict

def get_node_dicts(graph):
    return [get_node_dict(graph, n) for n in graph.nodes()]

def assort(graph):
    return nx.degree_assortativity_coefficient(graph)

def get_fi_vector(graph):
    return [get_fi(graph, n) for n in graph.nodes()]
