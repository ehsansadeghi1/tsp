#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the average weight of a Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)


def average(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Sum of weights of all n*(n-1)/2 edges.
    sum_of_weights = 0
    for i in range(n):
        for j in range(i):
            sum_of_weights += g[i][j]['weight']
    return 2*sum_of_weights / (n-1)

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

print(average(g))