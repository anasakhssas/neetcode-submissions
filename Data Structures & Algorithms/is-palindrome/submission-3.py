class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = [c.lower() for c in s if c.isalnum()]
        inv_ls = ls[::-1]
        for i in range(len(ls)) :
            if (ls[i] == inv_ls[i]):
                continue
            else :
                return False
        return True