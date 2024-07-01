# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left , right = 0, 0
        curSum, res = 0, 0
        maps = {}
        while right<len(nums):

            while left<right and len(maps)>=k  :
                curSum-=nums[left]
                maps.pop(nums[left])
                left+=1

            curSum+=nums[right]
            maps[nums[right]] = right
            print(maps)


            if len(maps)==k:
                res = max(res, curSum)
            right+=1

            # res = max(res, curSum)
            # print(res,curSum, "DDD")
            # while right-left+1>k:
            #     print(left-right+1,curSum )
            #     left+=1
            #     curSum-=nums[left]
        print(res, curSum)







# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15

nums = [1,5,4,2,9,9,9]
k = 3
# nums = [4,4,4]
# k = 3
Solution().maximumSubarraySum(nums, k)