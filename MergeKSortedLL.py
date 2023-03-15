class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        v1 = l1.val
        v2 = l2.val
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1+v2+carry

            carry = val // 10 
            val =  val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return dummy.next
