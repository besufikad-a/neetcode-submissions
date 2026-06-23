class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            missing = target - v
            new = nums [i+1:]
            if missing in new:
                if missing == v:
                    return [i, new.index(missing) + i + 1]
                return [i, nums.index(missing)]