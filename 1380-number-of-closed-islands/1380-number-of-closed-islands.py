class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        # 1) Mark all land (0) connected to the boundary as visited (open islands)
        for i in range(m):
            for j in (0, n-1):
                if grid[i][j] == 0 and not visited[i][j]:
                    bfs(i, j)
        for j in range(n):
            for i in (0, m-1):
                if grid[i][j] == 0 and not visited[i][j]:
                    bfs(i, j)

        # 2) Count interior components of 0's not visited yet (closed islands)
        count = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0 and not visited[i][j]:
                    bfs(i, j)
                    count += 1
        return count
            
            