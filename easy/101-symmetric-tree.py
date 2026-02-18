# https://leetcode.com/problems/symmetric-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.cmp(root.left, root.right)

    def cmp(self, left: Optional[TreeNode], right: Optional[TreeNone]) -> bool:

        if left == None and right == None:
            return True

        if left == None or right == None:
            return False

        return (
            left.val == right.val and
            self.cmp(left.left, right.right) and
            self.cmp(left.right, right.left)
        )
