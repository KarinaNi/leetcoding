import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('\W+','', s )
        s = s.lower()
        print(s)
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1

        return True



sol = Solution()
s = "racecar"
print(sol.isPalindrome(s))  # expected true

sol = Solution()
s = "carerace"
print(sol.isPalindrome(s)) # expected false

sol = Solution()
s = "baab"
print(sol.isPalindrome(s)) # expected true

sol = Solution()
s = "hoon"
print(sol.isPalindrome(s)) # expected false

sol = Solution()
s="Was it a car or a cat I saw?"
print(sol.isPalindrome(s)) # expected
