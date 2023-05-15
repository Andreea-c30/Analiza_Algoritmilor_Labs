import math
import networkx as nx
import matplotlib.pyplot as plt
import time
import time
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from prettytable import PrettyTable
x1 = PrettyTable(field_names=["Nr of nodes", "Time(s)"], title="Prim's method for sparse graphs")
x2 = PrettyTable(field_names=["Nr of nodes", "Time(s)"], title="Kruskal’s method for sparse graphs")


import random
import sys


def find_min_key(key, mst_set, num_nodes):
    min_key = sys.maxsize
    min_index = None
    for v in range(num_nodes):
        if key[v] < min_key and not mst_set[v]:
            min_key = key[v]
            min_index = v
    return min_index


def prim(graph):
    num_nodes = len(graph)

    key = [sys.maxsize] * num_nodes
    parent = [None] * num_nodes
    mst_set = [False] * num_nodes

    key[0] = 0
    parent[0] = -1

    for _ in range(num_nodes - 1):
        u = find_min_key(key, mst_set, num_nodes)
        mst_set[u] = True

        for v in range(num_nodes):
            if graph[u][v] and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    mst = []
    for v in range(1, num_nodes):
        mst.append((parent[v], v, graph[parent[v]][v]))

    return mst


def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]


def union(parent, rank, v1, v2):
    root1 = find(parent, v1)
    root2 = find(parent, v2)

    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            if rank[root1] == rank[root2]:
                rank[root1] += 1


def kruskal(graph):
    num_nodes = len(graph)

    # Create a list of edges
    edges = []
    for u in range(num_nodes):
        for v in range(u + 1, num_nodes):
            weight = graph[u][v]
            if weight != 0:
                edges.append((u, v, weight))

    # Sort the edges of the graph by weight in non-decreasing order
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # Create a dictionary to store the parent of each vertex
    parent = {v: v for v in range(num_nodes)}

    # Create a dictionary to store the rank of each vertex
    rank = {v: 0 for v in range(num_nodes)}

    # Initialize an empty minimum spanning tree
    mst = []

    for edge in sorted_edges:
        u, v, weight = edge

        # Check if including the edge forms a cycle in the minimum spanning tree
        if find(parent, u) != find(parent, v):
            mst.append(edge)
            union(parent, rank, u, v)

    return mst


def generate_random_graph(num_nodes, max_weight=10, edge_probability=0.5):
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() <= edge_probability:
                weight = random.randint(1, max_weight)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph




if __name__ == '__main__':
    times1, times2, times3, times4, times5 = [], [], [], [], []

    nr=[100,200,300,400,500,600,700,800,900,1000]
    for n in nr:
        print("\n\t\t",n, "nodes")
        graph = generate_random_graph(n)
        print("---------->For graph with",n," edges")
        print("Prim's's algorithm: ")
        start1 = time.perf_counter()
        prim(graph)
        end1 = time.perf_counter()
        total1 = end1 - start1
        x1.add_row([n, total1])
        times1.append(total1)
        print(f"\tTotal time of execution : {total1:.6f} sec")

        print("Kruskal’s algorithm: ")
        start2 = time.perf_counter()
        kruskal(graph)
        end2 = time.perf_counter()
        total2 = end2 - start2
        x2.add_row([n, total2])
        times2.append(total2)
        print(f"\tTotal time of execution : {total2:.6f} sec")





        # print the table with results for each method
    print("\n", x1)
    print("\n", x2)


    # print the graph for indense graphs
    plt.plot(nr, times1)
    plt.plot(nr, times2)


    plt.xlabel("Nr of nodes")
    plt.ylabel('time(s)')
    plt.legend(["Prim's algorithm", 'Kruskal’s algorithm'])
    plt.title(f'Graph of time for the algorithms')
    plt.show()


