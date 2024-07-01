class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l =0
        r = len(nums)-1
        i = 0

        while i <= r:
            if nums[i]==0:
                nums[i], nums[l] = nums[l], nums[i]
                i+=1
                l+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[i], nums[r] = nums[r], nums[i]
                # i+=1
                r-=1
            print(i, nums)




# Solution().sortColors([2,0,2,1,1,0])
# Solution().sortColors([2,0,1])
Solution().sortColors([1, 2,0])

