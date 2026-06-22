class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] == current:
                return True
            current = nums[i+1]
        return False
            

        