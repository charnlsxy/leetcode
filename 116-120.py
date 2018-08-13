# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution116_117:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        q1, q2 = [], []
        q1.append(root)
        current = q1
        while current:
            e = current.pop(0)
            other = q1 if current is q2 else q2
            if e.left:
                other.append(e.left)
            if e.right:
                other.append(e.right)
            if not current:
                current = other
            else:
                e.next = current[0]


class Solution118:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        src, prev = [], [1]
        src.append(prev)
        for i in range(numRows - 1):
            c = [1]
            for j in range(len(prev) - 1):
                c.append(prev[j] + prev[j + 1])
            c.append(1)
            src.append(c)
            prev = c
        return src


class Solution119:
    def generate(self, rowIndex):
        if not rowIndex:
            return [1]
        c = [1 for i in range(rowIndex + 1)]
        if rowIndex < 2:
            return c
        for i in range(3, rowIndex + 2):
            p = 1
            for j in range(1, i - 1):
                sp = c[j]
                c[j] = c[j] + p
                p = sp
        return c


class Solution120(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        ln = len(triangle)
        if ln == 1:
            return triangle[0][0]
        if ln == 2:
            return min(triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1])
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]
        for i in range(2, ln):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][i] += triangle[i-1][i-1]
            for j in range(1, len(triangle[i])-1):
                c = triangle[i][j]
                triangle[i][j] = min(c + triangle[i - 1][j], c + triangle[i - 1][j - 1])
        return min(triangle[ln-1])

a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(Solution120().minimumTotal(a))
# root = TreeLinkNode(1)
# root.left = TreeLinkNode(2)
# root.right = TreeLinkNode(3)
# root.left.left = TreeLinkNode(4)
# root.left.right = TreeLinkNode(5)
# root.right.left = TreeLinkNode(6)
# root.right.right = TreeLinkNode(7)
# Solution116_117().connect(root)
# print(root.val)
