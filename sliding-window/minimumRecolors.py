import sys
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        start = 0
        c = 0
        res = []
        m = sys.maxsize

        for end in range(len(blocks)):
            if blocks[end] == 'W':
                c+=1
            print(blocks[start:end+1])
            if end-start+1==k:
                m = min(m, c)
                if blocks[end] == 'W':
                    c-=1
                start+=1
        print(m)
            # print(end)
            # res.append(blocks[end])
# Input: 
blocks = "WBBWWBBWBW"
k = 7
# Output: 3
Solution().minimumRecolors(blocks, k)