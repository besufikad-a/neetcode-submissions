class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
            else:
                return False
        