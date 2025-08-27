class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for mask in range(1 << n):  # 2^n subsets
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            res.append(subset)
        return res
        