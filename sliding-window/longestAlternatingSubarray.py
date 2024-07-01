class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
        left, right = 0, 0
        N = len(nums)
        even = True
        res = 0

        while right <= (N-1) :
            if nums[right]>threshold:
                # close window and start new
                l=right+1
                right=l
                even=True
                continue
            
            if nums[right]%2 ^ even:
                res = max(res,right-left+1 )
                res+=1
                not even

            if nums[right]%2==0:
                #start window
                l=right
                right+=1
                even = False

            else:
                # close window and start new
                l=right+1
                right =l
                even = True
        print(res)

    # https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/description/
nums = [3,2,5,4]
threshold = 5
Solution().longestAlternatingSubarray(nums, threshold)