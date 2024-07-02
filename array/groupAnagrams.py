class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict 
        res = defaultdict(list)
        for item in strs:
            t = [0 for i in range(26)]
            for i in item:
                t[ord('a')-ord(i)]+=1
            print(t, item)
            res[tuple(t)].append(item)
        return res.values()


        

strs = ["eat","tea","tan","ate","nat","bat"]
Solution().groupAnagrams(strs)
        