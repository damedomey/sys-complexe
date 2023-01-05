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
