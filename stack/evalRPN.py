class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []

        for item in tokens:
            if item=="+":
                stack.append(stack.pop()+stack.pop())
            elif item=="-":
                a, b=stack.pop(),stack.pop()
                stack.append(b-a)

            elif item=="*":
                stack.append(stack.pop()*stack.pop())

            elif item=="/":
                a, b=stack.pop(),stack.pop()
                stack.append(b/a)
            else:
                stack.append(int(item)) 
        print(stack)
Solution().evalRPN(["2","1","+","3","*"])