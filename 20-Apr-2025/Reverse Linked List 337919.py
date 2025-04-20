# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = ListNode()
  
        cur = head

        while cur:
            if rev.next:
                tmp = rev.next
                rev.next = ListNode(cur.val, tmp)
            else:
                rev.next = ListNode(cur.val)
            cur = cur.next
        return rev.next







        