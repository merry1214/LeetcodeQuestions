class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        prev = [[0.0]*n for _ in range(n)]
        prev[row][column] = 1.0  # m = 0

        for _ in range(k):
            curr = [[0.0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if prev[i][j] == 0.0:
                        continue
                    p = prev[i][j] / 8.0
                    for di, dj in moves:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            curr[ni][nj] += p
            prev = curr
        return sum(map(sum, prev))
        