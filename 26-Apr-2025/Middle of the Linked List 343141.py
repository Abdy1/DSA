# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        pointer = head
        while pointer.next != None:
            length += 1
            pointer = pointer.next
        pointer = head
        for i in range(length//2):
            pointer = pointer.next
        return pointer

        print(length)
        