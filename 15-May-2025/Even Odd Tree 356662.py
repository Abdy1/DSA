# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([root])
        is_even_level = True 
        
        while q:
            level_size = len(q)
            prev_val = float('-inf') if is_even_level else float('inf')
            
            for _ in range(level_size):
                node = q.popleft()
                
                # Check value parity and order depending on level
                if is_even_level:
                    if node.val % 2 == 0 or node.val <= prev_val:
                        return False
                else:
                    if node.val % 2 != 0 or node.val >= prev_val:
                        return False
                
                prev_val = node.val  # Update previous value for comparison
                
                # Enqueue children for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            is_even_level = not is_even_level  # Toggle level parity
        
        return True