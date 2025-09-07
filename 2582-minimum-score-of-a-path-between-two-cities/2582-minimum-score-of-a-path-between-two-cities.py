class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = set()
        min_score = float("inf")

        
        q = deque([1])
        visited.add(1)

        while q:
            node = q.popleft()
            for nei, dist in graph[node]:
                min_score = min(min_score, dist)   
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return min_score
        