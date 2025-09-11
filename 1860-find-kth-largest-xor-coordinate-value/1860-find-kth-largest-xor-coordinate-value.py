class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        
        heap = []

        for i in range(m):
            for j in range(n):
                top = matrix[i-1][j] if i-1 >= 0 else 0
                left = matrix[i][j-1] if j-1 >= 0 else 0
                diag = matrix[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
            
                matrix[i][j] = matrix[i][j] ^ top ^ left ^ diag

                val = matrix[i][j]
                if len(heap) < k:
                    heapq.heappush(heap, val)
                else:
                    
                    if val > heap[0]:
                        heapq.heapreplace(heap, val)

    
        return heap[0]

            