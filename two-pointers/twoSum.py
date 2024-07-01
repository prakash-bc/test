class Solution(object):
    def twoSum(self, nums, target):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<right:
            tSum = nums[left]+nums[right]
            if tSum < target:
                left+=1
            elif tSum > target:
                right-=1
            else:
                print(target, tSum)
                return [left+1, right+1]
                return 


# height = [1,8,6,2,5,4,8,3,7]

# target = 9
# nums=[1,3,4,5,7,10,11]
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))
