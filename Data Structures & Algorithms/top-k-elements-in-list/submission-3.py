class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:      
        mom = {}
        for i in nums:
            if i in mom:
                mom[i] += 1
            else:
                mom[i] = 1
        new = []
        for m in range(k):
            max_key = max(mom, key=mom.get)
            new.append(max_key)
            mom.pop(max_key)
        return new
