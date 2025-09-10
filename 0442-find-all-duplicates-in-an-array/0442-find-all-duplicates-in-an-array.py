class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            index = abs(x) - 1
            if nums[index] < 0:
                res.append(abs(x))
            else:
                nums[index] = -nums[index]
        return res
            