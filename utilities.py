import random
from collections import Counter

import networkx as nx


def load_graph(filename) -> nx.Graph:
    """
    Load graph from file
    :param filename: Absolute path to the file to read
    :return g: the graph inside input file
    """
    g = nx.Graph()

    for line in open(filename, "r"):
        if len(line.split()) == 2:
            u, v = [int(x) for x in line.rstrip().split(" ")]
            g.add_edge(u, v)
    return g


def get_graph_sample(filename, node_limit=10000):
    """
    Load graph from file
    :param filename: Absolute path to the file to read
    :param node_limit: Limit of number of node in graph
    :return: A graph loaded from file or a sample with [node_limit] nodes
    """
    g = load_graph(filename)
    if g.number_of_nodes() > node_limit:
        sampled_nodes = random.sample(g.nodes, node_limit)
        g = g.subgraph(sampled_nodes)
        g = nx.subgraph(g, max(nx.connected_components(g), key=len))
    return g


def degre_moyen(g: nx.Graph) -> float:
    """
    Get average degree
    :param g: The graph
    :return: average degree
    """
    return (2 * len(g.edges)) / len(g.nodes)


def distribution_degree(g: nx.Graph):
    """
    Write the distribution of the degree in text file
    :param g: The graph
    :return:
        Nothing ! It just writes the distribution of degree in the file name [distribution_degree.txt]
        in data directory
    """
    n = len(g.nodes)
    count = Counter()
    for (node, degree) in g.degree():
        count[degree] += 1

    degree_count = sorted(count.items())

    with open("data/distribution_degree.txt", "w") as f:
        for (degree, count) in degree_count:
            f.write("{} {} {}\n".format(degree, count, count / n))
    # plot "data/big/distribution_degree.txt" using 1:2 with points pt 7 notitle


def get_nbr_triangles(g: nx.Graph):
    """
    Get the number of triangles in the graph
    :param g: The graph
    :return:
    """
    return sum(nx.triangles(g).values()) / 3


def get_node_importance(g: nx.Graph):
    """
    Get the importance of each node.
    The interval of importance is [0, 1]. 0 mean that the node isn't important.
    In contrast, 1 mean that he is most import, it is present on all shortest path.
    :param g: The graph
    :return: A dictionary of node importance keyed by the name of node. It is sorted by importance (most to least)
    """
    shortest_path = nx.shortest_path(g)

    c = Counter()
    nbr_of_couple = 0

    for source, _ in shortest_path.items():
        for target, path in _.items():
            if source < target:
                nbr_of_couple += 1
                for node in path:
                    if node not in [source, target]:
                        c[node] += 1

    importance = dict()
    for k, v in sorted(c.items(), key=lambda x: x[1], reverse=True):
        importance[k] = v / nbr_of_couple

    return importance
