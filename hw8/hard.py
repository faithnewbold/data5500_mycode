'''
Write a Python function that takes a NetworkX graph as input and returns the number of nodes in the graph that have a degree greater than 5
'''

import networkx as nx

def count_nodes(G):
    return G.number_of_nodes() #returns the number of nodes on the graph


G = nx.erdos_renyi_graph(n=10, p=0.3) #used to create random edges, with 10 nodes with a 30% probability of edge creation
print("edges:", G.edges)

degree_above_5 = sum(1 for _, degree in G.degree() if degree > 5) #adds up the number of nodes that are greater than 5

print("Number of nodes with a degree greater than 5:", degree_above_5)