class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
    def binSearch(self, nums, target, leftBais):
        left , right= 0, len(nums)-1
        i  =-1
        while left<=right:
            mid = (left+right)//2
            if target <nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = mid+1
            else:
                i = mid
                if leftBais:
                    right = mid-1
                else:
                    left = mid+1

        return i 
                    
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))