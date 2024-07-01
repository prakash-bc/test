from collections import defaultdict 

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res = defaultdict(list)
    for item in strs:
        temp = [0 for i in range(26)]
        for s in item:
            temp[ord('a')-ord(s)]+=1
        print(item,temp)
        res[tuple(temp)].append(item)
    print(res)

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)
        
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]