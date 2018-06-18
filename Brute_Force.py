#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
from itertools import permutations
import matplotlib.pyplot as plt

# =============================================================================
# This function takes as input a graph g.
# The function should return the weight of a shortest Hamiltonian cycle.
# You can iterate through all permutations of the set
# {0, ..., n-1} and find a cycle of the minimum weight.
# =============================================================================


def cycle_length(g, cycle):
    # Checking that the number of vertices in
    # the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()

    weight = g[cycle[0]][cycle[len(cycle)-1]]['weight']
    for i in range(len(cycle)-1):
        weight += g[cycle[i]][cycle[i+1]]['weight']
    return weight, cycle

def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    w = []
    # Iterate through all permutations of n vertices
    for cycle in permutations(range(n)):
        w += [cycle_length(g, cycle)]
    return min(w)

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
#nx.draw(g,with_labels=True)
#plt.show()

print(all_permutations(g))
