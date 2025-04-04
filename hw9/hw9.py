import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations

import networkx as nx
from networkx.classes.function import path_weight

import matplotlib.pyplot as plt

# Define the API URL
url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin,litecoin,ripple,cardano,bitcoin-cash,eos&vs_currencies=eth,btc,ltc,xrp,ada,bch,eos"

# creating a coin names and tickers dictionary
ticker_map = {
    "bitcoin": "btc",
    "ethereum": "eth",
    "litecoin": "ltc",
    "ripple": "xrp",
    "cardano": "ada",
    "bitcoin-cash": "bch",
    "eos": "eos"
}

response = requests.get(url)
data = response.json()

# Convert the API response keys to ticker format
converted_data = {ticker_map[coin]: rates for coin, rates in data.items()}

# Generate all unique (ticker1, ticker2) pairs
currencies = list(converted_data.keys())
edges = []
g = nx.DiGraph()

for c1, c2 in permutations(currencies, 2):  # All possible pairs except (x, x)
    if c2 in converted_data[c1]:  # Check if conversion rate exists
        rate = converted_data[c1][c2]
        edges.append((c1, c2, rate)) #adding all the edge pairs to the edges list

# Print results
# for edge in edges:
#     print(edge)

g.add_weighted_edges_from(edges) #adding the edges to the graph


# Track min and max
min_factor = float('inf')
max_factor = float('-inf')
min_paths = ()
max_paths = ()

# Now traverse graph
for source, target in permutations(currencies, 2):
    print(f"\npaths from  {source} to {target} ----------------------------------")
    for path in nx.all_simple_paths(g, source=source, target=target):
        try: #use a try and except in case there aren't paths both to and from each
            f_weight = 1.0
            for i in range(len(path) - 1):
                f_weight *= g[path[i]][path[i+1]]['weight'] #calculate the path weight
            f_weight = round(f_weight, 10)
        except KeyError:
            print(f"Forward path does not exist for: {path}")
            continue  # skip this path

        # Reverse path and weight/paths coming from the node
        try:
            reverse_path = list(reversed(path))
            r_weight = 1.0
            for i in range(len(reverse_path) - 1):
                r_weight *= g[reverse_path[i]][reverse_path[i+1]]['weight']
            r_weight = round(r_weight, 10)
        except KeyError:
            print(f"Reverse path does not exist for: {reverse_path}")
            continue  # skip this pair and move to the next

        # multiple the paths to and from the node
        factor = round(f_weight * r_weight, 10)

        # Output
        print(path, f_weight)
        print(reverse_path, r_weight)
        print(factor)

        # Update min/max
        if factor < min_factor:
            min_factor = factor
            min_paths = (path, reverse_path)
        if factor > max_factor:
            max_factor = factor
            max_paths = (path, reverse_path)

# print the final output
print("\nSmallest Paths weight factor: ", min_factor)
print("Paths: ", min_paths[0], min_paths[1])

print("\nGreatest Paths weight factor: ", max_factor)
print("Paths: ", max_paths[0], max_paths[1])
