class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0

        vowel = {'a','e','i','o','u'}
        l, cnt = 0, 0
        for r in range(len(s)):
            cnt +=1 if s[r] in vowel else 0
            if r - l + 1 > k:
                cnt -= 1 if s[l] in vowel else 0
                l += 1
            res = max(res, cnt)
            if res == k:
                return k
        return res
