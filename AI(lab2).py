# 1. Use BFS/DFS for grid based maze, find the shortest path using BFS, use DFS to explore all possible paths and report one valid path
# 2. Root finder using bi-directional BFS and DFS
# 3. Visualize the graphs using Python libraries

# from collections import deque

# grid = [  
#     [1,1,0,1],
#     [1,1,1,0],
#     [0,1,1,1],
#     [1,0,1,1]
# ]

# rows = len(grid)
# cols = len(grid[0])
# start = (0,0)
# end = (3,3)

# def bfs(grid, start, end):
#     q = deque([start])
#     visited = {start: None}
#     while q:
#         x,y = q.popleft()
#         if (x,y) == end:
#             path = []
#             cur = end
#             while cur:
#                 path.append(cur)
#                 cur = visited[cur]
#             return path[::-1]
#         for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nx,ny = x+dx, y+dy
#             if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
#                 if (nx,ny) not in visited:
#                     visited[(nx,ny)] = (x,y)
#                     q.append((nx,ny))
#     return None

# def dfs(grid, start, end):
#     stack = [start]
#     visited = {start: None}
#     while stack:
#         x,y = stack.pop()
#         if (x,y) == end:
#             path = []
#             cur = end
#             while cur:
#                 path.append(cur)
#                 cur = visited[cur]
#             return path[::-1]
#         for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nx,ny = x+dx, y+dy
#             if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
#                 if (nx,ny) not in visited:
#                     visited[(nx,ny)] = (x,y)
#                     stack.append((nx,ny))
#     return None

# print("BFS shortest path:", bfs(grid,start,end))
# print("DFS valid path:", dfs(grid,start,end))


# from collections import deque
# graph = {
#     'A':['B','C'],
#     'B':['A','D'],
#     'C':['A','D'],
#     'D':['B','C','E'],
#     'E':['D']
# }

# def bidirectional_bfs(graph, start, end):
#     if start == end:
#         return [start]

#     front = {start: None}
#     back = {end: None}
#     q1 = deque([start])
#     q2 = deque([end])

#     while q1 and q2:
#         f = q1.popleft()
#         for n in graph[f]:
#             if n not in front:
#                 front[n] = f
#                 q1.append(n)
#             if n in back:
#                 return build(front, back, n)

#         b = q2.popleft()
#         for n in graph[b]:
#             if n not in back:
#                 back[n] = b
#                 q2.append(n)
#             if n in front:
#                 return build(front, back, n)

#     return None

# def build(front, back, meet):
#     path = []
#     x = meet
#     while x:
#         path.append(x)
#         x = front[x]
#     path.reverse()
#     x = back[meet]
#     while x:
#         path.append(x)
#         x = back[x]
#     return path

# print("Bidirectional BFS path:", bidirectional_bfs(graph,'A','E'))


# dfs route:def dfs_route(graph, start, end, visited=None):
# def dfs_route(graph, start, end, visited=None):
#     if visited is None:
#         visited = set()
#     if start == end:
#         return [start]
#     visited.add(start)
#     for n in graph[start]:
#         if n not in visited:
#             path = dfs_route(graph,n,end,visited)
#             if path:
#                 return [start] + path
#     return None

# print("DFS route:", dfs_route(graph,'A','E'))


# graph visualization
# import networkx as nx
# import matplotlib.pyplot as plt

# G = nx.Graph()
# G.add_edges_from([
#     ('A','B'),
#     ('A','C'),
#     ('B','D'),
#     ('C','D'),
#     ('D','E')
# ])

# nx.draw(G, with_labels=True, node_size=1000)
# plt.show()

# from collections import deque
# graph = {
#     'A':['B','C'],
#     'B':['A','D'],
#     'C':['A','D'],
#     'D':['B','C','E'],
#     'E':['D']
# }

# # -------- BFS --------
# def bfs(graph, start, end):
#     q = deque([start])
#     visited = {start}
#     count = 0

#     while q:
#         node = q.popleft()
#         count += 1
#         if node == end:
#             return count
#         for n in graph[node]:
#             if n not in visited:
#                 visited.add(n)
#                 q.append(n)
#     return count

# # -------- DFS --------
# def dfs(graph, start, end, visited=None, count=0):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     count += 1
#     if start == end:
#         return count
#     for n in graph[start]:
#         if n not in visited:
#             c = dfs(graph, n, end, visited, count)
#             if c:
#                 return c
#     return None

# -------- Bi-directional BFS --------
# def bidirectional_bfs(graph, start, end):
#     q1 = deque([start])
#     q2 = deque([end])
#     v1 = {start}
#     v2 = {end}
#     count = 0

#     while q1 and q2:
#         a = q1.popleft()
#         count += 1
#         for n in graph[a]:
#             if n in v2:
#                 return count
#             if n not in v1:
#                 v1.add(n)
#                 q1.append(n)

#         b = q2.popleft()
#         count += 1
#         for n in graph[b]:
#             if n in v1:
#                 return count
#             if n not in v2:
#                 v2.add(n)
#                 q2.append(n)
#     return count

# -------- Comparison --------
# print("BFS nodes explored:", bfs(graph,'A','E'))
# print("DFS nodes explored:", dfs(graph,'A','E'))
# print("Bi-directional BFS nodes explored:", bidirectional_bfs(graph,'A','E'))


import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C','E'],
    'E':['D']
}

G = nx.Graph()

for node in graph:
    for n in graph[node]:
        G.add_edge(node, n)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_size=1500)
plt.show()
