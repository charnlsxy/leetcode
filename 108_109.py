# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def convert(node):
            a = []
            while node:
                a.append(node.val)
                node = node.next
            return a
        nums = convert(head)
        if not nums:
            return None
        def build(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            if len(arr) == 2:
                e = TreeNode(arr[1])
                e.left = TreeNode(arr[0])
                return e
            i = len(arr)//2
            e = TreeNode(arr[i])
            e.left = build(arr[:i])
            e.right = build(arr[i+1:])
            return e
        return build(nums)
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        def build(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            if len(arr) == 2:
                e = TreeNode(arr[1])
                e.left = TreeNode(arr[0])
                return e
            i = len(arr)//2
            e = TreeNode(arr[i])
            e.left = build(arr[:i])
            e.right = build(arr[i+1:])
            return e
        return build(nums)

a = [-10,-3,0,5,9]
e = Solution().sortedArrayToBST(a)
print(e)

