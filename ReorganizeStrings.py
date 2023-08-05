# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxHeap = [[-val , key] for key, val in count.items()]

        heapq.heapify(maxHeap)

        res = ""
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt,char]
 
        return res
                
# Runtime 40 ms Beats 92.20%
# Memory 16.3 MB Beats 79.14%            


