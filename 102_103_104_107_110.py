# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 102 103
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q1 = []
        q2 = []
        q = q1
        rst = []
        current = []
        q.append(root)
        travel = True
        while q:
            e = q.pop(0)
            if travel:
                current.append(e.val)
            else:
                current.insert(0, e.val)
            tq = q2 if q is q1 else q1
            if e.left:
                tq.append(e.left)
            if e.right:
                tq.append(e.right)
            if not q:
                rst.append(current)
                current = []
                q = q1 if q is q2 else q2
                travel = not travel
        return rst

    # 104
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max1(r):
            if not r:
                return 0
            if not r.left and not r.right:
                return 1
            return max(max1(r.left) + 1, max1(r.right) + 1)

        return max1(root)

    # 110
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def max1(r):
            if not r:
                return 0
            if not r.left and not r.right:
                return 1
            return max(max1(r.left) + 1, max1(r.right) + 1)
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(max1(root.left) - max1(root.right)) < 2

    # 107
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q1, q2, rst, current = [], [], [], []
        q = q1
        q.append(root)
        while q:
            e = q.pop(0)
            current.append(e.val)
            tq = q2 if q is q1 else q1
            if e.left:
                tq.append(e.left)
            if e.right:
                tq.append(e.right)
            if not q:
                rst.append(current)
                current = []
                q = q1 if q is q2 else q2
        rst.reverse()
        return rst


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrderBottom(root))
