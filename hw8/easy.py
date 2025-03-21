'''
Write a Python function that takes a NetworkX graph as input and returns the number of nodes in the graph.
'''

import networkx as nx

def count_nodes(G):
    return G.number_of_nodes() #returns the number of nodes on the graph


G = nx.erdos_renyi_graph(n=10, p=0.3) #used to create random edges, with 10 nodes, with a 30% probability of edge creation
print("edges:", G.edges)

print("number of nodes:", count_nodes(G))