class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(temperatures)
        stack = []
        for index, temp in  enumerate(temperatures):
            while stack and temp> stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = index-stackI
            stack.append([temp, index])
            print(stack)
        print(res)



        
temperatures = [73,74,75,71,69,72,76,73]
Solution().dailyTemperatures(temperatures)