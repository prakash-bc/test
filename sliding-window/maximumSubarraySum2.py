class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, 0
        currSum, ans =0, 0
        n  = len(nums)
        maps = {}
        res = 0
        while right <n:
            while left< right and len(maps)>=k:
                print('DDDDD',maps, currSum )
                currSum -=nums[left]
                maps.pop(nums[left])
                left+=1
                print('DDDDDDONE',maps, currSum )


            currSum +=nums[right]
            maps[nums[right]] = True
            right+=1
            print(maps)

            if len(maps)==k:
                res = max(res, currSum)
        print(res)
        return res

        



# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15

nums = [1,5,4,2,9,9,9]
k = 3
# nums = [4,4,4]
# k = 3
Solution().maximumSubarraySum(nums, k)