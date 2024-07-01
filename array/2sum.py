class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for index in range(len(nums)):
            item=nums[index]
            diff = target-item
            if diff in res:
                return [res.get(diff), index]
            print(diff)
            res[item] = index
        print(res)
# Input: 
nums = [2,7,11,15]
target = 9
# Output: [0,1]

print(Solution().twoSum(nums, 9), "DD")