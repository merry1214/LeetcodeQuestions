class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = DSU(n)

        row_map = {}   
        col_map = {}   

        for i, (r, c) in enumerate(stones):
            if r in row_map:
                dsu.union(i, row_map[r])
            else:
                row_map[r] = i

            if c in col_map:
                dsu.union(i, col_map[c])
            else:
                col_map[c] = i

        
        roots = set(dsu.find(i) for i in range(n))
        components = len(roots)
        return n - components