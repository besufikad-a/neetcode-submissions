class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:      
        mom = {}
        for i in nums:
            mom[i] = mom.get(i,0) + 1
        new = []
        for m in range(k):
            max_key = max(mom, key=mom.get)
            new.append(max_key)
            mom.pop(max_key)
        return new
