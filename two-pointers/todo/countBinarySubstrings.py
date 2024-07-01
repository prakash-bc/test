class Solution(object):
    def countBinarySubstrings(self, s):
        current = 1
        pre = 0
        for i in range(1, len(s)):
            print(i)
            if s[i-1]==s[i]:
                current+=1
            else:
                print(s[pre:i], "str", min(current, pre))
                pre = current
                current = 1

        print(min(current, pre), "SSS")
s = "00110011"
Solution().countBinarySubstrings(s)
//FIX ME