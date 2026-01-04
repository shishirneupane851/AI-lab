from collections import deque    #simple city map

graph = {
    "Home": ["Shop", "Park"],
    "Shop": ["Home", "Mall"],
    "Park": ["Home", "Hospital"],
    "Mall": ["Shop", "Hospital"],
    "Hospital": ["Park", "Mall"]
}

def bfs(start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()

        if node == goal:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # Reconstruct shortest path
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent[cur]

    return list(reversed(path))

path = bfs("Home", "Hospital")
print(path)
