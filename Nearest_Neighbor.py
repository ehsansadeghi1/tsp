#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
# =============================================================================
# This function takes as input a graph g.
# The function should return the weight of the nearest neighbor heuristic,
# which starts at the vertex number 0,
# and then each time selects a closest vertex.
# =============================================================================


def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times
    for j in range(n - 1):
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        for v in g.nodes():  # g.nodes() returns nodes of graph g
            if (v not in path) and (g[current_node][v]['weight'] < min_edge):
                min_edge = g[current_node][v]['weight']
                next_node = v
            # decide if v is a better candidate than next_node.
            # If it is, then update the values of next_node and min_edge
        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(n - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight, path

g = nx.Graph()
g.add_edge(0, 1, weight=6)
g.add_edge(1, 2, weight=2)
g.add_edge(2, 3, weight=3)
g.add_edge(3, 0, weight=2)
g.add_edge(0, 2, weight=5)
g.add_edge(1, 3, weight=1)
g.add_edge(0, 4, weight=3)
g.add_edge(1, 4, weight=1)
g.add_edge(2, 4, weight=1)
g.add_edge(3, 4, weight=2)

print(nearest_neighbors(g))

