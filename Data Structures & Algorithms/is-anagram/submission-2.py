class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            count = 0
            co = 0
            for i in range(len(s)):
                n = s[i]

                if n not in t:
                    return False
                for m in s:
                    if m == n:
                        count += 1
                for d in t:
                    if d == t:
                        co +=1
                if count == co:
                    return True    
            return True
        return False