class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(11, slow, fast)

            if slow==fast:
                break
        print(slow, fast)


        slow2=0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow==slow2:
                print(slow)
                break


nums = [1,3,4,2,2]
Solution().findDuplicate(nums)