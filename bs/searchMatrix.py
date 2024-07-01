class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        left , right = 0, rows*cols-1
        print(left, right)
        while left<= right:
            mid = (left+right)//2
            print(mid)
            r, c = mid//cols,  mid%cols
            print(mid, r, c)
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                left = mid+1

            else:
                right = mid-1

            # left+=1
            # right-=1
        return False


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))
#  rows, cols = len(matrix), len(matrix[0])
#         low, high = 0, rows*cols-1
#         while low <= high:
#             mid = (low+high)//2
#             row, col = mid//cols, mid%cols
#             print(row, col, "mid", mid, matrix[row][col], "low+hi", low, high)
#             if matrix[row][col] ==target:
#                 return True
#             elif matrix[row][col] <target:
#                 low=mid+1
#             else:
#                 high=mid-1
#         return False