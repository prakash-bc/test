class Solution(object):
    def threeSum(self, nums):
        res = []
        for index, item in enumerate(nums):
            if index>0 and nums[index-1]==item:
                continue
            print(item)
            l , r = index+1, len(nums)-1
            while l<r:
                tsum = item + nums[l]+nums[r]
                if tsum < 0:
                    l+=1
                elif tsum >0:
                    r-=1
                else:
                    res.append([item , nums[l],nums[r]])
                    print(res)
                    l+=1
                    r-=1
                    # r-=1
                    # while  nums[l-1]==nums[l] and l<r:
                    #     l+=1
        return res 

# height = [1,8,6,2,5,4,8,3,7]

# target = 9
# nums=[1,3,4,5,7,10,11]
nums = [-1,0,1,2,-1,-4]
# [-1,0,1,2,-1,-4]

print(Solution().threeSum(nums))
