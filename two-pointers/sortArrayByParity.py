class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = 0
        for i in range(len(nums)):
            print(nums[i])
            if nums[i]%2==0:
                nums[left], nums[i]= nums[i], nums[left]
                left+=1
        print(nums)

    
nums = [3,1,2,4]
Solution().sortArrayByParity(nums)