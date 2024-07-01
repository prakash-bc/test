# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right =0
        n = len(s)
        m = {}
        max_size = 0
        while right<n:
            m[s[right]]  = 1+m.get(s[right], 0)
            print(m)
            right+=1
            max_size = max(max_size, right-left+1)
            while right-left+1-max(m.values())>=k:
                left+=1
                m[s[left]]-=1
                if m[s[left]]==0:
                    del m[s[left]]
            print(max_size, s[:right], right-left+1, max(m.values()), right-left+1-max(m.values()))




# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
s = "ABAB"
k = 2
Solution().characterReplacement(s, k)