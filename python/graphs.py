from collections import defaultdict, deque

# Array of Edges (Directed) [Start, End]
n = 8
A =  [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Array of Edges -> Adjacency Matrix
M = []
for i in range(n):
    M.append([0] * n) # Since there are 8 nodes, create a nxn matrix

for u, v in A:
    M[u][v] = 1 # Append connections to adjanency graph

# If graph was undirected
# M[v][u] = 1

print(M)

# Using Adjacency List

D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    # Undirected: D[v].append(u)

print(D)

# Recursive DFS

def dfs_recursive(node):
    print(node) # Processing
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

source = 0
seen = set()
seen.add(source)

dfs_recursive(source)

# Iterative DFS

source = 0
seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)

# BFS - O(V + E)

source = 0
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)