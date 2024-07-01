class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(index, subset):
            print(index, subset)
            if index>=len(nums):
                res.append(subset)
                return
            dfs(index+1, subset+[nums[index]])
            dfs(index+1, subset)

        dfs(0, [])
        print(res, len(res))

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        print(nums, "111")
        if len(nums)==1:
            return [nums.copy()]
        for i in range(len(nums)):
            print(nums, "l")
            temp = nums.pop(0)
            print(nums, "l1temp", temp)

            perms = self.permute(nums)
            for p in  perms:
                p.append(temp)
            res.extend(perms)
            nums.append(temp)
        print(nums, "222")
        return res


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(index, curr, total):
            if total==target:
                res.append(curr[:]) 
                return 
            if total>target or index>=len(candidates):
                return
            print(index, curr, curr+[candidates[index]])
            dfs(index, curr+[candidates[index]], total+candidates[index])
            dfs(index+1, curr, total)
        dfs(0, [], 0)
        print(res)
    def letterCombinations(self, digits):
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def bactrack(index, curr):
            if len(curr)==len(digits):
                res.append(curr)
                return 
            m = digitToChar[digits[index]]
            for c in m:
                bactrack(index+1 ,curr+c)
        bactrack(0, "")
        print(res)



            

        
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    #   1 2 3
nums = [1,2,3]
# Solution().subsets(nums)
candidates = [2,3,6,7]
target = 7
# print(Solution().combinationSum(candidates, target))

digits = "23"
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
print(Solution().letterCombinations(digits))
