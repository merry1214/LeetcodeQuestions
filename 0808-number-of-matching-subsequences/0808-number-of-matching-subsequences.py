from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        buckets = defaultdict(list)
        
       
        for w in words:
            buckets[w[0]].append(iter(w[1:]))  

        count = 0
        for ch in s:
           
            waiting = buckets[ch]
            buckets[ch] = []
            
            for it in waiting:
                nxt = next(it, None)
                if nxt:
                    buckets[nxt].append(it)
                else:
                    count += 1
        return count
