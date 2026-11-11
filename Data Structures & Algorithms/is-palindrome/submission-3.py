class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = s.lower()
        k = []
        for i in new:
            if (97 <= ord(i) <= 122) or (48 <= ord(i) <= 57):
                k.append(i)
        return k == k[::-1]

        
