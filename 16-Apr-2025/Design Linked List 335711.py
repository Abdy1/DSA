# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None  # <-- key fix

    def get(self, index: int) -> int:
        current = self.head
        while index and current:
            current = current.next
            index -= 1
        return current.val if current else -1                        

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.head = ListNode(val, self.head)
            return 
        current = self.head
        for _ in range(index - 1):
            if not current:
                return
            current = current.next
        if current:
            new_node = ListNode(val, current.next)
            current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if not current or not current.next:
                return 
            current = current.next
        if current and current.next:
            current.next = current.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)