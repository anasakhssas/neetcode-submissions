class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = [c.lower() for c in s if c.isalnum()]
        l,r = 0 , len(ls) - 1
        while l < r :
            if (ls[l] == ls[r]) :
                l = l+1
                r = r-1
            else :
                return False

        return True