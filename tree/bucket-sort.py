class Solution(object):
    def sortArray(self, nums):
        """
        https://leetcode.com/problems/sort-an-array/
        """
        bucket = {k:0 for k in range(min(nums), max(nums)+1)}
        for i in nums:
          bucket[i] = 1+bucket.get(i, 0)
        res = []
        for key, val in bucket.items():
          if val!=0:
            res.extend([key]*val)
        print(res)
    def topKFrequent(self, nums, k):
        "https://leetcode.com/problems/top-k-frequent-elements/description/"
        bucket = {k:0 for k in range(min(nums), max(nums)+1)}
        for i in nums:
          bucket[i] = 1+bucket.get(i, 0)
        print(bucket)
        freq = [[]  for i in range(len(nums)+1)]
        for key, val in bucket.items():
          freq[val].append(key)
        print(freq)
        res  =[]
        for i in range(len(freq)-1, 0, -1):
          for n in freq[i]:
            res.append(n)
            if len(res)==k:
              return res
    def frequencySort(self, s):
      "https://leetcode.com/problems/sort-characters-by-frequency/"
      freq = [[]  for i in range(len(s)+1)]
      count = {}
      for n in s:
        count[n] = 1+count.get(n, 0)
      print(count)

      for k, v in count.items():
        freq[v].append(k)
      print(freq)

      res = []
      for i in range(len(freq)-1, 0, -1):
        for item in freq[i]:
          res.extend([item]*i)
      print(res)






# nums = [5,2,3,1]
# Solution().sortArray(nums)
nums = [1,1,1,2,2,3]
k = 2
res = Solution().topKFrequent(nums, k)
print(res)
res = Solution().frequencySort('tree')
print(res)