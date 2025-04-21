# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ansHead = ans
        while list1 and list2:
            if list1.val > list2.val:
                ans.next = ListNode(list2.val, None)
                ans = ans.next
                list2 = list2.next
            else:
                ans.next = ListNode(list1.val, None)
                ans = ans.next
                list1 = list1.next
        if list1:
            ans.next = list1
        if list2:
            ans.next = list2
        return ansHead.next


        