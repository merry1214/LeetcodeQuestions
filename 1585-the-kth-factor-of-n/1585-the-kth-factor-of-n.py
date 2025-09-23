class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []
        i = 1
        
        while i * i <= n:
            if n % i == 0:
                small.append(i)
                if i * i != n:
                    large.append(n // i)
            i += 1

        
        if k <= len(small):
            return small[k-1]

        
        k -= len(small)
        if k <= len(large):
            return large[-k]  

        return -1
        