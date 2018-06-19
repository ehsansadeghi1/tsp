#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx

def approximation(g):
    # =============================================================================
    # This function takes as input a graph g and
    # Returns a 2-approximation of an optimal Hamiltonian cycle.
    # =============================================================================
    # returns a Minimum Spanning Tree T of G.
    T = nx.minimum_spanning_tree(g, weight='weight')
    # Gives a list of vertices of the given graph in depth-first preorder.
    dfs = nx.dfs_preorder_nodes(T)
    listnode = []
    for item in dfs:
        listnode += [item]
    weight = g[listnode[0]][listnode[len(listnode)-1]]['weight']
    for i in range(len(listnode)-1):
        weight += g[listnode[i]][listnode[i+1]]['weight']

    return weight

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

print(approximation(g))
