# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l, r = self.minDepth(root.left), self.minDepth(root.right)
        mn = min(l, r)
        mx = max(l, r)
        return mn + 1 if mn > 0 else mx + 1

    # 112
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # 113
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        rst = []

        def path(root, sum, pre):
            if not root:
                return
            tp = pre.copy()
            tp.append(root.val)
            if not root.left and not root.right and root.val == sum:
                rst.append(tp)
            if root.left:
                path(root.left, sum - root.val, tp)
            if root.right:
                path(root.right, sum - root.val, tp)

        path(root, sum, [])
        return rst

    # 114
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def change(p):
            if not p:
                return
            if not p.left and not p.right:
                return pch
            if not p.left:
                return change(p.right)
            if not p.right:
                l = p.left
                p.left = None
                p.right = l
                return change(l)
            ll = change(p.left)
            pr = p.right
            p.right = p.left
            p.left = None
            ll.right = pr
            return change(p.right)
        change(root)
        print(1)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

print(Solution().flatten(root))
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6