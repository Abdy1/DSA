# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.travers(res,root)
        return res
    def travers(self,l:List[int],node:Optional[TreeNode]):
        if node:
            self.travers(l,node.left)
            self.travers(l,node.right)
            l.append(node.val)
        