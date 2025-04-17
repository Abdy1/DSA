# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        lenn = 0
        while cur:
            lenn += 1
            cur = cur.next
        
        first_half = head
        second_half = head
  
        for _ in range(lenn//2):
            second_half = second_half.next

        dummy = ListNode()        
        while second_half:
            new_node = ListNode(second_half.val)
            new_node.next = dummy
            dummy = new_node 
            second_half = second_half.next

        maxx = float('-inf')
        left = first_half
        right = dummy
        for _ in range(lenn//2):
            maxx = max(maxx, (left.val+right.val))
            left = left.next
            right = right.next
        return maxx

   







        