class Solution121(object):
    # err un consider condition like 2,4,1
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        mx, mn, mxi, mni = prices[0], prices[0], 0, 0
        for i in range(1, len(prices)):
            if mx < prices[i]:
                mx = prices[i]
                mxi = i
            if mn > prices[i]:
                mn = prices[i]
                mni = i
                if mxi < mni:
                    mxi = 0
                    mx = 0
        if mxi > mni:
            return mx - mn
        return 0

    # fine, time limit =.=
    def maxProfit2(self, prices):
        mx = 0
        for i in range(1, len(prices)):
            for j in range(i):
                k = prices[i] - prices[j]
                if k > 0 and k > mx:
                    mx = k
        return mx

    def maxProfit(self, prices):
        mx = 0
        mni = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[mni]:
                mni = i
                continue
            if prices[i] - prices[mni] > mx:
                mx = prices[i] - prices[mni]
        return mx


class Solution309(object):
    # buy 0 sell 1 cool 2
    # and time limit again qaq
    def maxProfit(self, prices):
        if not prices:
            return 0
        ln = len(prices)
        if ln == 1:
            return prices[0]
        q1, q2 = [(0, 0, 0, None)], []
        for i in prices:
            while q1:
                e = q1.pop(0)
                if e[2] == 1:
                    q2.append((e[0] + i, 's', e[2] - 1, e))
                if e[1] != 's' and e[2] == 0:
                    q2.append((e[0] - i, 'b', e[2] + 1, e))
                q2.append((e[0], 'c', e[2], e))
            q1, q2 = q2, q1
        mx = 0
        # m = ()
        for i in q1:
            if i[0] > mx and i[2] >= 0:
                mx = i[0]
                # m = i
        # while m[3] != None:
        #     print(m[:-1])
        #     m = m[3]
        return mx


def test309():
    tests = [
        [1, 2, 3, 0, 2],
        [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15,
         11, 94]
    ]
    for i in tests:
        print(Solution309().maxProfit(i))

def test121():
    tests = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 4, 7, 8, 5, 9, 2, 54, 5],
        [2, 4, 1], []
    ]
    for i in tests:
        print(Solution121().maxProfit(i))


test309()
