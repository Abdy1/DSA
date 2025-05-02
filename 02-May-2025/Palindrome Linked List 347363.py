# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_temp = slow.next
            slow.next = prev
            prev = slow
            slow = next_temp

        first = head
        second = prev 
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True