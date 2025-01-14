import igraph
import sys
from collections import defaultdict


edges = [line.split('-') for line in sys.stdin.read().splitlines()]

adjacency = defaultdict(set)
for a, b in edges:
    adjacency[a].add(b)
    adjacency[b].add(a)
    
labels = list(adjacency.keys())
edges = [[i, j] for i in range(len(labels)) for j in range(len(labels)) if labels[j] in adjacency[labels[i]]]

graph = igraph.Graph(len(labels), edges)
cliques = graph.cliques()

count = 0
for clique in cliques:
    if len(clique) != 3:
        continue
    for c in clique:
        if labels[c][0] == 't':
            count += 1
            break

print(count)

print(','.join(sorted(labels[v] for v in sorted((len(q), q) for q in cliques)[-1][1])))



# Implement cliques algorithm

