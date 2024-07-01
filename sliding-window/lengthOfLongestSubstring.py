# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {}

        left = 0
        right  = 0
        n = len(s)
        max_size =-1
        while right<n:
            # if len(res)<right-left+1:
            res[s[right]] = 1+res.get(s[right], 0)
            max_size     = max(max_size, len(res))
            print(res, len(res), max_size)
            while  len(res) and (right-left+1 > len(res)):
                res[s[left]]-=1
                if  res[s[left]]==0:
                    del res [s[left]]
                left+=1
            right+=1
        return max_size

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
s = "abcabcbb"

Solution().lengthOfLongestSubstring(s)