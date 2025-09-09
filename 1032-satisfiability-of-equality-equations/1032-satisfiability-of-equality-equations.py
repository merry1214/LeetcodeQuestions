class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))  # 26 lowercase letters

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

       
        for eq in equations:
            if eq[1:3] == "==":
                a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
                union(a, b)

       
        for eq in equations:
            if eq[1:3] == "!=":
                a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
                if find(a) == find(b): 
                    return False

        return True
        