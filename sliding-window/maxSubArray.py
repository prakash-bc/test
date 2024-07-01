# https://leetcode.com/problems/maximum-subarray/description/
class Solution(object):
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     maxSub = nums[0]   
    #     curSum =0
    #     for item in nums:
    #         if curSum<0:
    #             curSum = 0
    #         curSum+=item
    #         maxSub= max(curSum,maxSub)
    #     print(maxSub)


    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left , right=0, 0
        curSum, res = 0, -float("INF")
        while right<len(nums):
            curSum +=nums[right]
            right+=1
            res = max(res, curSum)
            print(res , "DDD")
            while curSum<=0 and left<right and left<len(nums):
                curSum-=nums[left]
                left+=1
        print(res)
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# nums = [1,2,-4,7,2]
nums = [-1]
Solution().maxSubArray(nums)

# 1 2 -4 7 2/
