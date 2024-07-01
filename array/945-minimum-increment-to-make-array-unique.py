class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        res = 0
        for i in range(1, len(nums)):
            print(nums,  nums[i-1], nums[i], nums[i-1]+1-nums[i])
            if nums[i-1]>= nums[i]:
                res+=nums[i-1]+1-nums[i]
                nums[i] = nums[i-1]+1
            print(res, "###")
nums=[3,2,1,2,1,7]
Solution().minIncrementForUnique(nums)
1 3 5
2 4 7
