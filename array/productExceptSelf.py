
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n  = len(nums)
    # left = [1 for i in nums]
    # right = [1 for i in nums]
    # print(nums, "###")
    # for i in range(1, len(nums)):
    #     left[i] = nums[i-1]*left[i-1]
    # print(left)

    # for i in range(len(nums)-2,-1, -1):
    #     right[i] = nums[i+1]*right[i+   1]
    # print(right, "###")

    prefix = [1 for i in nums]
    # for i in range(n):
    #     ans[i] = left[i]*right[i]
    # print(ans, "###")
    for i in range(1, len(nums)):
        prefix[i] = nums[i-1]*prefix[i-1]
    post = 1
    for i in range(len(nums)-1,-1, -1):
        print(nums[i], nums[i-1])
        prefix[i] = prefix[i]*post
        post *= nums[i]
    print(prefix)
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
productExceptSelf([1,2,3,4])
# 1 2 3 4 - input
# 1 1 2 6 - prefixsum
# 24,12,8,6

# 4 3 2 1


# [1, 2, 6, 24]

# 24 24 12 4