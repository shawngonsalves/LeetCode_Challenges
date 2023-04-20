class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        p = list(palindrome)

        for i in range(len(p)):
            if p[i] !="a":
                p[i] = "a"
                break
        if p!=p[::-1]: return "".join(p)
        p = list(palindrome)
        for i in range(len(palindrome)-1,-1, -1):
            if p[i] == "a":
                p[i] = "b"
                break
        return "".join(p)
        
