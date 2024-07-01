def topKFrequent(nums, k):
    count={}
    for item in nums:
        count[item] = 1+count.get(item, 0)

    bucket = [[] for i in range(len(nums)+1)]
    print(bucket)
    for v, c in count.items():
        bucket[c].append(v)
    print(bucket)   
    res = []

    for i in range(len(bucket)-1, 0, -1):
        for b in bucket[i]:
            res.append(b)
            print(res, len(res), k)
            if len(res)==k:
                return res
        # if len(bucket[i]):
        #     print(i, bucket[i])



nums = [1,1,1,2,2,3]
k = 2
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
print(topKFrequent(nums, 2))
