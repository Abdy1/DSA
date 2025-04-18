# Problem: Print the Elements of a Linked List - https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

def printLinkedList(head):
    while head:
        print(head.data)
        head = head.next
if __name__ == '__main__':