class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i,v in enumerate(nums):
            missing = target - v
            if missing in seen:
                return [seen[missing], i]
            seen[v] = i
