# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/submissions/1050786618/class Solution(object):
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {}
        left = 0
        right = 0
        n = len(s)
        ans = 0

        while right<n:
            res[s[right]] = 1+res.get(s[right], 0)
            print(res)
            right+=1

            while res.get('a') and res.get('b') and res.get('c'):
                print("DDDDDDDDDDDDDD",res, len(s)-right)
                ans+=1
                res[s[left]]-=1
                left+=1
        print(ans, "SSSSSSSSSS")
        


s= "abcabc"
output = 10
Solution().numberOfSubstrings(s)