class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=1
        rtype = 0
        while r<len(prices):
            diff =prices[r]-prices[l]
            rtype = max(rtype, diff)
            print(diff, rtype)
            if diff<0:
                l+=1
            r+=1
        print(rtype
        )

            

# Input: prices = [7,1,5,3,6,4]
# Output: 5
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))