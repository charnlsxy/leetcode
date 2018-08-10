# Definition for a binary tree node.
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        arr = Queue()
        arr.put(root.left)
        arr.put(root.right)
        while True:
            if arr.empty():
                return True
            lg = arr.get()
            rg = arr.get()
            if lg is rg:  # both none
                continue
            elif lg is not None and rg is not None and lg.val == rg.val:
                arr.put(lg.left)
                arr.put(rg.right)
                arr.put(lg.right)
                arr.put(rg.left)
            else:
                return False


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(2)
    t.left.right = TreeNode(3)
    t.right.left = TreeNode(3)
    print(Solution().isSymmetric(t))
