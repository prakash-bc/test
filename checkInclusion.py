# https://leetcode.com/problems/permutation-in-string/    
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
# or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # dictionary = dict(Counter(s2))
        # print(dictionary)
        n , m = len(s1), len(s2)
        if n>m:
            return False
        s1Count = [0]*26
        s2Count = [0]*26
        for i in range(n):
            s1Count[ord(s1[i])-ord('a')]+=1
            s2Count[ord(s2[i])-ord('a')]+=1
        if s1Count==s2Count:
            return True
        j=0
        for i in range(n, m):
            print(s2[i], s2[i-n], i-n, j, "XX", )
            s2Count[ord(s2[i])-ord('a')]+=1
            s2Count[ord(s2[i-n])-ord('a')]-=1
            if s1Count==s2Count:
                return True
            j+=1
        return False

# https://leetcode.com/problems/permutation-in-string/solutions/2449916/91-performance-python-solution-using-sliding-window

s1 = "ab"
s2 = "eidbaooo"
Solution().checkInclusion(s1, s2)