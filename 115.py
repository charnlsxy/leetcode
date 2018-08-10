class Solution:
    # time limit
    def numDistinct1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        matrix = {}

        def get(s, t, sd, td):
            if len(t) == 0:
                return 0
            sum = 0
            if len(t) == 1:
                for i in s:
                    if i == t:
                        sum += 1
                return sum
            if len(s) == 1:
                return 1 if s[0] == t[0] else 0
            for i in range(len(s) - len(t) + 1):
                # if matrix[sd + i][td] > 0:
                if str(sd + i) + ":" + str(td) in matrix:
                    return matrix[sd + i][td]
                if s[i] == t[0]:
                    p = get(s[i + 1:], t[1:], sd + i + 1, td + 1)
                    matrix[str(sd + i + 1) + ":" + str(td + 1)] = p
                    sum += p
            return sum

        a = get(s, t, 0, 0)
        return a

    def numDistinct(self, s, t):
        if len(t) > len(s) or len(t) == 0:
            return 0
        current = [0 for i in range(len(s))]
        for i in range(len(s)):
            p = i-1 if i > 0 else 0
            current[i] = current[p]
            if s[i] == t[0]:
                current[i] += 1
        for j in range(len(t)-1):
            pre = current
            current = [0 for i in range(len(s))]
            n = len(s) - j - 1
            for k in range(n):
                i = k + j + 1
                p = i-1
                if s[i] == t[j+1]:
                    current[i] = current[p] + pre[p]
                else:
                    current[i] = current[p]

        return current[-1]

# S, T = "rabbbit", "rabbit"
# S = "babgbag"
# T = "bag"

# S = "aaaaaaaaaaaaa"
# T = "aaa"
S = "aaaaa"
T = "aaa"
print(Solution().numDistinct(S, T))

# print(matrix)
