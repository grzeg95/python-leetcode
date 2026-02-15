# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []

        if root.left == None and root.right == None:
            return [root.val]

        result = []

        result += self.inorderTraversal(root.left)
        result += [root.val]
        result += self.inorderTraversal(root.right)

        return result
