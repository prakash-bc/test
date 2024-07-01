class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        while left<= right:
            while left<right and not self.alphaNum(s[left]):
                left+=1
            while left<right and not self.alphaNum(s[right]):
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
    def alphaNum(self, c):
        return ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9') or ord('a') <= ord(c) <= ord('z')
s = "race a car"
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))