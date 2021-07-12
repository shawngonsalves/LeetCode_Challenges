'''
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return head
        
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length+=1
        
        k = k % length
        if k==0:
            return head
        curr = head
        for i in range(length-k-1):
            curr = curr.next
        
        newhead = curr.next
        curr.next = None
        tail.next = head
        return newhead
