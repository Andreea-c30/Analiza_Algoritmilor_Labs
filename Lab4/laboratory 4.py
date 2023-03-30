import math
import networkx as nx
import matplotlib.pyplot as plt
import time
#adjacency list
#balanced graph
graph = {
        '5': ['2', '8'],
        '2': ['1', '4'],
        '8': ['7', '9'],
        '1': [],
        '4': ['3'],
        '7': [],
        '9': ['6', '10'],
        '3': [],
        '6': [],
        '10': []
}
#unbalanced graph
graph2 = {
  '1': ['2', '3'],
  '2': [],
  '3': ['4', '5'],
  '4': [],
  '5': ['6', '7'],
  '6': [],
  '7': ['8', '9'],
  '8': [],
  '9': ['10'],
  '10': []
}
 #define the starting node
root1=5
root2=1

visited1 = set()
visited2 = set()

#function for dfs
def dfs(visited, graph, node):

    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs( visited, graph, neighbour)


queue = []

#function for bfs
def bfs( graph, node):
  visited = [] #list for visited nodes
  visited.append(node)
  queue.append(node)
  # creating loop to visit each node
  while queue:
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

if __name__ == '__main__':
    times1, times2, times3, times4, times5 = [], [], [], [], []
    print("For the balanced tree:")
    start1 = time.perf_counter()
    print("Following is the Breadth-First Search")

    bfs(graph, str(root1))
    end1 = time.perf_counter()
    total1 = end1 - start1
    print(f"\nTotal time of execution : {total1:.6f} sec")

    print("For the balanced tree:")
    start2 = time.perf_counter()
    print("Following is the Depth-First Search")
    dfs(visited1,graph, str(root1))
    end2 = time.perf_counter()
    total2 = end2 - start2
    print(f"\nTotal time of execution : {total2:.6f} sec")

    print("\nFor the unbalanced tree:")
    start3 = time.perf_counter()
    print("Following is the Breadth-First Search")
    bfs(graph2, str(root2))
    end3 = time.perf_counter()
    total3 = end3 - start3
    print(f"\nTotal time of execution : {total3:.6f} sec")

    print("\nFor the unbalanced tree:")
    start4 = time.perf_counter()
    print("Following is the Depth-First Search")
    dfs(visited2, graph2, str(root2))
    end4 = time.perf_counter()
    total4 = end4 - start4
    print(f"\nTotal time of execution : {total4:.6f} sec")

   #create an empty graph
    G = nx.Graph()

    #add the edges to the graph
    for node in graph:
        G.add_edges_from([(node, child) for child in graph[node]])

    plt.title('Balanced Tree')
    #draw the graph and mark the starting node as root1
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_nodes(G, pos, nodelist=[str(root1)], node_color='r', node_size=500)


    plt.show()
    #create an empty graph
    G2 = nx.Graph()

    #add the edges to the graph
    for node in graph2:
        G2.add_edges_from([(node, child) for child in graph2[node]])
    plt.title('Unbalanced Tree')
    #draw the graph and mark the starting node as root2
    pos = nx.spring_layout(G2)
    nx.draw(G2, pos, with_labels=True)
    nx.draw_networkx_nodes(G2, pos, nodelist=[str(root2)], node_color='r', node_size=500)


    plt.show()

    #define the data for the graph
    x = ['BFS_b', 'DFS_b']
    x1 = ['BFS_u', 'DFS_u']
    b = [total1,total2]
    u=[total3,total4]

    #create the bar chart
    plt.bar(x, b)
    plt.bar(x1, u)

    #add labels and title to the graph
    plt.xlabel('Method')
    plt.ylabel('time(s)')
    plt.title('Time analysis chart')
    plt.legend(['for balanced tree','for unbalanced tree'])
    #show the graph
    plt.show()
