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
x1 = PrettyTable(field_names=["Nr of nodes", "Time(s)"], title="Dijkstra method for sparse graphs")
x2 = PrettyTable(field_names=["Nr of nodes", "Time(s)"], title="Floyd Warshall method for sparse graphs")
x3 = PrettyTable(field_names=["Nr of nodes", "Time(s)"], title="Dijkstra method for dense graphs")
x4 = PrettyTable(field_names=["Nr of nodes", "Time(s)"], title="Floyd Warshall method for dense graphs")


def dijkstra_method(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    visited = set()

    while len(visited) != len(graph):
        min_node = None
        for node in dist:
            if node not in visited:
                if min_node is None or dist[node] < dist[min_node]:
                    min_node = node
        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            new_dist = dist[min_node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
    return dist

def floyd_warshall(graph):
    nodes = list(graph.keys())
    n = len(nodes)
    dist = np.full((n, n), np.inf)

    for i, node in enumerate(nodes):
        dist[i, i] = 0
        for neighbor, weight in graph[node].items():
            j = nodes.index(neighbor)
            dist[i, j] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]

    return {nodes[i]: {nodes[j]: dist[i, j] for j in range(n)} for i in range(n)}


def generate_rare_graph(num_nodes, max_weight=10, density=0.2):
    # Create a dense graph
    graph = {i: {} for i in range(num_nodes)}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, max_weight)
            graph[i][j] = weight
            graph[j][i] = weight

    # Remove edges randomly to create a sparse graph
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() > density:
                del graph[i][j]
                del graph[j][i]

    return graph

def generate_dense_graph(num_nodes, max_weight=10):
    graph = {i: {} for i in range(num_nodes)}
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            weight = random.randint(1, max_weight)
            graph[i][j] = weight
            graph[j][i] = weight
    return graph


if __name__ == '__main__':
    times1, times2, times3, times4, times5 = [], [], [], [], []

    # Sparse graph
    nr=[10,20,30,40,50,60,70,80,90]
    for n in nr:
        print("\n\t\t",n, "nodes")
        graph = generate_rare_graph(n)
        print("---For the sparse graph---")
        print("Dijkstra's algorithm: ")
        start1 = time.perf_counter()
        dijkstra_method(graph, 0)
        end1 = time.perf_counter()
        total1 = end1 - start1
        x1.add_row([n, total1])
        times1.append(total1)
        print(f"\tTotal time of execution : {total1:.6f} sec")

        print("Floyd Warshall algorithm: ")
        start2 = time.perf_counter()
        floyd_warshall(graph)
        end2 = time.perf_counter()
        total2 = end2 - start2
        x2.add_row([n, total2])
        times2.append(total2)
        print(f"\tTotal time of execution : {total2:.6f} sec")



        graph = generate_dense_graph(n)
        print("---For the dense graph---")
        print("Dijkstra's algorithm: ")
        start3 = time.perf_counter()
        dijkstra_method(graph, 0)
        end3 = time.perf_counter()
        total3 = end3 - start3
        x3.add_row([n, total3])
        times3.append(total3)
        print(f"\tTotal time of execution : {total3:.6f} sec")

        print("Floyd Warshall algorithm: ")
        start4 = time.perf_counter()
        floyd_warshall(graph)
        end4 = time.perf_counter()
        total4 = end4 - start4
        x4.add_row([n, total4])
        times4.append(total4)
        print(f"\tTotal time of execution : {total4:.6f} sec")

        # print the table with results for each method
    print("\n", x1)
    print("\n", x2)
    print("\n", x3)
    print("\n", x4)

    # print the graph for indense graphs
    plt.plot(nr, times1)
    plt.plot(nr, times2)


    plt.xlabel("Nr of nodes")
    plt.ylabel('time(s)')
    plt.legend(['Dijkstra', 'Floyd Warshall'])
    plt.title(f'Graph of time for sparse graphs')
    plt.show()

    # print the graph for dense graphs
    plt.plot(nr, times3)
    plt.plot(nr, times4)

    plt.xlabel("Nr of nodes")
    plt.ylabel('time(s)')
    plt.legend(['Dijkstra', 'Floyd Warshall'])
    plt.title(f'Graph of time for dense graphs')
    plt.show()
