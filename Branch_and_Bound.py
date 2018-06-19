#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx


def lower_bound(g, sub_cycle):
    # =============================================================================
    # This function computes a lower bound on the length of Hamiltonian cycles
    # starting with vertices in the list sub_cycle.
    # =============================================================================
    current_weight = 0  # current_weight: The weight of the current path.
    for i in range(len(sub_cycle)-1):
        current_weight += g[sub_cycle[i]][sub_cycle[i + 1]]['weight']
    unused = []  # a graph which only contains vertices not used by g
    for v in g.nodes():
        if v not in sub_cycle:
            unused += [v]
    h = g.subgraph(unused)

    """
    minimum_spanning_edges(G, weight='weight', data=True)
    A minimum spanning tree is a subgraph of the graph (a tree)
    with the minimum sum of edge weights.
    Uses Kruskal’s algorithm.
    """
    t = list(nx.minimum_spanning_edges(h))
    mst_weight = 0  # weight of a minimum spanning tree
    for e in t:
        mst_weight += h.get_edge_data(e[0], e[1])['weight']
    """
    If the current sub_cycle contains no vertices or all vertices,
    then lower bound is the sum of the weight of a minimum spanning tree
    and the current weight.
    """
    if len(sub_cycle) == 0 or len(sub_cycle) == g.number_of_nodes():
        return mst_weight + current_weight
    """
    If the current sub_cycle is not trivial, then we can also
    add the weight of two edges connecting the vertices
    from sub_cycle and the remaining part of the graph.
    """
    s = sub_cycle[0]   # s is the first vertex of the sub_cycle
    t = sub_cycle[-1]  # t is the last vertex of the sub_cycle

    """
    The minimum weight of an edge connecting a vertex
    from outside of sub_sycle to s.
    """
    ll = []
    for v in g.nodes():
        if v not in sub_cycle:
            ll.append(g[v][s]['weight'])
    min_to_s_weight = min(ll)
    del ll
    """
    The minimum weight of an edge connecting the vertex t
    to a vertex from outside of sub_cycle.
    """
    a = []
    for v in g.nodes():
        if v not in sub_cycle:
            a.append(g[t][v]['weight'])
    min_from_t_weight = min(a)
    del a
    """
    Any cycle which starts with sub_cycle must be of length:
    the weight of the edges from sub_cycle +
    the min weight of an edge connecting sub_cycle and the remaining vertices +
    the min weight of a spanning tree on the remaining vertices +
    the min weight of an edge connecting the remaining vertices to sub_cycle.
    """
    lower_bound = current_weight + min_from_t_weight + mst_weight + min_to_s_weight
    return lower_bound


# The branch and bound procedure takes
# 1. a graph g;
# 2. the current sub_cycle, i.e. several first vertices of cycle under consideration.
# Initially sub_cycle is empty;
# 3. currently best solution current_min, so that we don't even consider paths of greater weight.
# Initially the min weight is infinite


def branch_and_bound(g, sub_cycle=None, current_min=float("inf")):
    # If the current path is empty, then we can safely assume
    # that it starts with the vertex 0.
    if sub_cycle is None:
        sub_cycle = [0]

    # If we already have all vertices in the cycle,
    # then we just compute the weight of this cycle and return it.
    if len(sub_cycle) == g.number_of_nodes():
        weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])
        weight = weight + g[sub_cycle[-1]][sub_cycle[0]]['weight']
        return weight

    # Now we look at all nodes which aren't yet used in sub_cycle.
    unused_nodes = list()
    for v in g.nodes():
        if v not in sub_cycle:
            unused_nodes.append((g[sub_cycle[-1]][v]['weight'], v))

    # We sort them by the distance from the "current node"
    # -- the last node in sub_cycle.
    unused_nodes = sorted(unused_nodes)
    for (d, v) in unused_nodes:
        assert v not in sub_cycle
        extended_subcycle = list(sub_cycle)
        extended_subcycle.append(v)
        # For each unused vertex, we check if there is any chance to
        # find a shorter cycle if we add it now.
        if lower_bound(g, extended_subcycle) < current_min:
            # If there is such a chance, we add the vertex to the current cycle,
            # and proceed recursively.
            # If we found a short cycle, then we update the current_min value.
            # The procedure returns the shortest cycle length.
            current_min = branch_and_bound(g, extended_subcycle, current_min)
            if len(sub_cycle) == g.number_of_nodes() and current_weight < current_min:
                current_min = branch_and_bound(g, extended_subcycle, current_weight)
    return current_min


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

print(branch_and_bound(g, sub_cycle=None, current_min=float("inf")))