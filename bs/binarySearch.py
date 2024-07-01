class Solution(object):
    def search(self, nums, target):
        n = len(nums)

        l = 0
        r = n-1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                print(m)
                # return m
        return -1
    
# Input: nums = [-1,0,3,5,9,12], target = 9
        
nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums,target ))