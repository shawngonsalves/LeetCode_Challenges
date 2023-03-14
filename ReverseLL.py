class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next

            curr.next = prev
            
            prev= curr
            curr= nxt
        return prev
