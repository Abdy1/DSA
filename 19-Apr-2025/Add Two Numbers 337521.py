# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        ansp = ans
        overflow = 0
        l1p = l1
        l2p = l2

        while l1p or l2p or overflow:
            val = overflow
            if l1p:
                val += l1p.val
                l1p = l1p.next
            if l2p:
                val += l2p.val
                l2p = l2p.next
            overflow = val//10
            ansp.next = ListNode(val%10)
            ansp = ansp.next
        return ans.next
            

        
        