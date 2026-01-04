import heapq

grid = [
    [1,1,1,1],
    [1,0,1,1],
    [1,1,1,0],
    [1,1,1,1]
]

rows = len(grid)
cols = len(grid[0])

start = (0,0)
treasure = (3,3)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def best_first_search(grid, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start))
    visited = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = visited[current]
            return path[::-1]

        x, y = current
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                if (nx,ny) not in visited:
                    visited[(nx,ny)] = current
                    heapq.heappush(pq, (heuristic((nx,ny), goal), (nx,ny)))

    return None

path = best_first_search(grid, start, treasure)
print("Treasure path:", path)
