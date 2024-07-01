class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        first = 0
        second = k
        n = len(nums)
        res = []
        min1, min2 = nums[0], nums[0]
        while second < n:
            second+=1
            if second-first>k:
                first+=1
            min2 = min1
            min1 = min(min1, nums[second-1])
            print("min2, min1", min2, min1)
            print(nums[first:second], "##")



# Explanation: There are 3 subarrays with size k = 3. 
# The first subarray is [1, -1, -3] and the 2nd smallest negative integer is -1. 
# The second subarray is [-1, -3, -2] and the 2nd smallest negative integer is -2. 
# The third subarray is [-3, -2, 3] and the 2nd smallest negative integer is -2.
# nums, k, x
nums = [1,-1,-3,-2,3]
k = 3
x = 2
Solution().getSubarrayBeauty(nums, k, x)