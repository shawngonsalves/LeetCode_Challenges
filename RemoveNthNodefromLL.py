'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        
        while r and n>0:
            r = r.next
            n-=1
            
        while r:
            l = l.next
            r = r.next
            
        l.next = l.next.next
        
        return dummy.next
'''
Runtime: 44 ms, faster than 14.16% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.3 MB, less than 14.61% of Python3 online submissions for Remove Nth Node From End of List.
'''