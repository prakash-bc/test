import heapq
# https://leetcode.com/problems/kth-largest-element-in-an-array/
def findKthLargest( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    print(nums)
    for index, val in enumerate(nums):
        nums[index]= -val
        print(index, val)
    # print(nums[:k])
    heapq.heapify(nums)
    # print(nums, "dddd")
    # print(nums[k-1])
    res = 0
    while k>0:
        res = -heapq.heappop(nums)
        k-=1
    print(res)



        
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example
nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))