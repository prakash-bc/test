class Solution(object):
    def makeSmallestPalindrome(self, s):
        res = list(s)
        l, r = 0, len(s)-1
        while l<=r:
            print(s[l], s[r], ord(s[l]), ord(s[r]))
            if ord(s[l])<ord(s[r]):
                res[r] = s[l]
            else:
                res[l] = s[r]

            l+=1
            r-=1
        return "".join(res)

s = "egcfe"
Solution().makeSmallestPalindrome(s)