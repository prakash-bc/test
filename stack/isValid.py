class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        stack = []
        for item in s:
            if item not in m:
                stack.append(item)
                print(item, stack, "DDDD")
            else:
                if not stack or stack[-1]!= m[item]:

                    return False
                print(stack[-1], m[item], "ZZZZZ")
                # if stack[-1]!=m[item]
        print("DD", stack)
        return not stack
            # else:
            #     pass
s = "()"
# s = "()"
print(Solution().isValid(s))