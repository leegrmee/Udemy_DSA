"""
Height-Balanced
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

"""

# first approach


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution(object):
#     def isBalanced(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: bool
#         """

#         cur = root
#         l = []
#         r = []
#         if root is None:
#             return True

#         while cur:
#             if cur.left:
#                 l.append(cur.left.val)
#                 cur= cur.left
#             elif cur.right:
#                 r.append(cur.right.val)
#                 cur=cur.right
#             else:
#                 return True
#         dif= len(l) - len(r)
#         if dif > abs(1):
#             return False
#         return True


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(root):
            if not root:
                return [True, 0]
            l, r = dfs(root.left), dfs(root.right)
            balanced = l[0] and r[0] and abs(l[1] - r[1] <= 1)
            return [balanced, 1 + max(l[1], r[1])]

        return dfs(root)[0]


s = Solution()
print(s.isBalanced([3, 9, 20, 0, 0, 15, 7]))
