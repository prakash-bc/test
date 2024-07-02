# https://leetcode.com/problems/container-with-most-water/description/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # return 1
        # res = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         h = min(height[i], height[j])
        #         res = max(res, (j-i)*h)
        # print(res)

        l = 0
        r = len(height)-1
        res = 0
        c=0
        while l<r:
            h = min(height[l], height[r])
            print(h, "minh")
            res = max(res, (r-l)*h)
            print(res, "res")
            if height[l]< height[r]:
                l+=1
            else:
                r-=1
        print(res,"DDDD")
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))