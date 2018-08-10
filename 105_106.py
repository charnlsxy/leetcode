# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree1(self, po, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # try travl method and faild
        # ele = TreeNode(0)
        # p = ele
        # for i in inorder:
        #     ele.right = TreeNode(i)
        #     ele = ele.right
        # p = p.right
        # for i in preorder:
        #     if p.val == i:
        #         p = p.left
        #
        # return ele

        # time exceed arr.index() cost too much time
        # def build(arr):
        #     if not arr:
        #         return None
        #     if len(arr) == 1:
        #         return TreeNode(arr[0])
        #     mn = len(preorder)+1
        #     for i in arr:
        #         mn = min(mn, preorder.index(i))
        #     e = TreeNode(preorder[mn])
        #     k = arr.index(e.val)
        #     preorder.remove(e.val)
        #     e.left, e.right = build(arr[:k]), build(arr[k + 1:])
        #     return e
        # return build(inorder)
        def build(pre, arr):
            if not arr:
                return None
            n = len(arr)
            if n == 1:
                return TreeNode(arr[0])
            k = arr.index(pre[0])
            e = TreeNode(arr[k])
            e.left, e.right = build(pre[1:len(arr[:k]) + 1], arr[:k]), build(pre[len(arr[:k]) + 1:], arr[k + 1:])
            return e

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build2(back, arr):
            if not arr:
                return None
            n = len(arr)
            if n == 1:
                return TreeNode(arr[0])
            k = arr.index(back[-1])
            e = TreeNode(arr[k])
            e.left, e.right = build2(back[:len(arr[:k])], arr[:k]), build2(back[len(arr[:k]):-1], arr[k + 1:])
            return e

        return build2(postorder, inorder)


m = [9,3,15,20,7]
b = [9,15,7,20,3]

Solution().buildTree(b, m)
# 16,808 平方公里
# 2171 万
