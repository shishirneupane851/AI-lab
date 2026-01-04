import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = []
    heapq.heappush(pq, (manhattan(start, goal), start, [start]))

    while pq:
        h, current, path = heapq.heappop(pq)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)
        r, c = current

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                if (nr, nc) not in visited:
                    heapq.heappush(
                        pq,
                        (manhattan((nr, nc), goal), (nr, nc), path + [(nr, nc)])
                    )
    return None

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
treasure = (3, 3)

path = best_first_search(grid, start, treasure)
print("Path to treasure:", path)
