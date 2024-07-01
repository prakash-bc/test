# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/submissions/1023185671/
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        k=3
        left , right = 0,0
        n = len(s)
        m = {}

        while right < n:
            while right-left+1>k:
                print("DDDDD",right, left,  right-left+1)
                if s[left] in m:
                    m[s[left]]-=1
                    # del m[s[left]]
                left+=1

            m[s[right]]=1+m.get(s[right], 0)
            print(m)
            if right-left+1==k:
                print(s[left:right+1])
            right+=1


s = "xyzzaz"
s= "aababcabc"
Solution().countGoodSubstrings(s)