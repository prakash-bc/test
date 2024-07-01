class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        print('###############')
        # res = 0
        # for i in range(1, len(nums)):
        #     if nums[i]<=nums[i-1]:
        #         nums[i] = nums[i-1]+1
        #         res+=1
        # print(res, nums)
        # return res==1
        cnt_violations = 0
        for i in range(1, len(nums)):
            print(nums)
            if nums[i-1]<=nums[i]:
                continue
            if cnt_violations==1:
                return False
            cnt_violations+=1
            if i>=2 and nums[i-2]> nums[i]:
            # print(nums[i], nums[i-1])
                nums[i]=nums[i-1]
        print(cnt_violations, nums)
        return cnt_violations==1
        
# nums=[4,2,3]
# # nums=[3, 4,2,3]

# print(Solution().checkPossibility(nums))

nums=[1]
print(Solution().checkPossibility(nums))


# nums=[2,2,1]
# print(Solution().checkPossibility(nums))


# nums=[3,4,2,3]
# print(Solution().checkPossibility(nums))
# 