# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[l]<=nums[mid]:
                if target> nums[mid] or target< nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            
            else:
                if target< nums[mid] or target> nums[r]:
                    r=mid-1
                else:
                    l=mid+1

        return -1


nums = [4,5,6,7,0,1,2]
target = 0
 
print(Solution().search(nums, target))