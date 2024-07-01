import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = r

        while l<=r:
            k = (r+l)//2
            totalTime=0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
                # totalTime+=p/k
            if totalTime<=h:
                res = totalTime
                l = k+1
            else:
                r = k-1

            print(totalTime)
        print(res, "DDD")

# Input: piles = [3,6,7,11], h = 8
     
piles = [3,6,7,11]
h = 8
Solution().minEatingSpeed(piles, h)