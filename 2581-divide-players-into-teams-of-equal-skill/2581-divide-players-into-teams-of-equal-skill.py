class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total_product = 0
        target = skill[0] + skill[-1]

        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target:
                return -1
            total_product += skill[i] * skill[n - 1 - i]

        return total_product
        