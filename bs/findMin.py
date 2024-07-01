# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0 , len(nums)-1
        res = nums[0]
        while start<end:
            mid = (start+end)//2
            res = min(res, nums[mid])

            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid-1
        print(res, start)
        return min(res, nums[start])

print(Solution().findMin([3,4,5,1,2]))