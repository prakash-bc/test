from collections import Counter

class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        t = Counter(target)
        a = Counter(arr)
        print(t, dict(t))
        print(a, dict(t))
        return t==a



        
target = [1,2,3,4]
arr = [2,4,1,3]
Solution().canBeEqual(target, arr)
# Input: target = [1,2,3,4], arr = [2,4,1,3]
# Output: true