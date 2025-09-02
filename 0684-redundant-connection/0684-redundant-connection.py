class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        
       
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False   
            parent[rootX] = rootY
            return True
        
        
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            
            # If union fails, that's the redundant edge
            if not union(u, v):
                return [u, v]

        