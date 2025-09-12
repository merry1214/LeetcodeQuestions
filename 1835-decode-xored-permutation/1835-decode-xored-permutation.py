class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        
        
        total = 0
        for i in range(1, n + 1):
            total ^= i
        
        
        oddXor = 0
        for i in range(1, len(encoded), 2):
            oddXor ^= encoded[i]
        
        
        first = total ^ oddXor
        
        perm = [first]
        for num in encoded:
            perm.append(perm[-1] ^ num)
        
        return perm
        