class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] not in t:
                    return False
            return True
        return False