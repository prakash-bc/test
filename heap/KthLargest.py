import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.minHeap = nums
        # print(self.minHeap)
        heapq.heapify(nums)
        # print(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        # print(self.minHeap, "INIT END")

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minHeap, val)
        print(k, "DD")
        if len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        # print(self.minHeap)
        return self.minHeap[0]



        


# Your KthLargest object will be instantiated and called as such:
nums = [4, 5, 8, 2]
# k = 3
obj = KthLargest(3, nums)

param_1 = obj.add(3)