"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# first approach
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur_node = root
        while cur_node:
            if p.val > cur_node.val and q.val > cur_node.val:
                cur_node = cur_node.right

            elif p.val < cur_node.val and q.val < cur_node.val:
                cur_node = cur_node.left

            else:
                return cur_node


# second approach

# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         cur = root
#         while cur:
#             if p.val > cur.val and q.val > cur.val:
#                 cur = cur.right
#             elif p.val < cur.val and q.val < cur.val:
#                 cur = cur.left
#             else:
#                 return cur
