# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # res = []

        # while head:
        #     res.append(head.val)
        #     head = head.next
        
        # left, right = 0, len(res) - 1

        # while left <= right:
        #     if res[left] != res[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        # return res


        mid, end = head, head

        # find mid
        while end and end.next:
            end = end.next.next
            mid = mid.next
        #reverse 2nd half of LL
        prev = None
        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp

        #actual checking
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
            
        return True

# Runtime 719 ms Beats 87.76%
# Memory 41.4 MB Beats 67.3%        

        


