class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i): chr(i) for i in range(97, 123)} 

        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return
            if rootX < rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY

        
        for a, b in zip(s1, s2):
            union(a, b)

       
        return "".join(find(ch) for ch in baseStr)
        