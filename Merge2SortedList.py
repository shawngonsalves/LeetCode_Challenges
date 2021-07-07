'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 
Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
'''

class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b


'''
Runtime: 40 ms, faster than 50.54% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.4 MB, less than 29.87% of Python3 online submissions for Merge Two Sorted Lists.

'''