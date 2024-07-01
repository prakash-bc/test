# https://leetcode.com/problems/time-based-key-value-store/description/
class TimeMap(object):

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values)-1
        while l<=r:
            m = (l+r//2)
            if values[m][1] <=timestamp:
                res = values[m][0]
                l = m+1
            else:
                r  = m-1
        return res

# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

        


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar",1)
obj.set("foo","bar2",2)

param_2 = obj.get("foo",1)
print(param_2)

param_2 = obj.get("foo",3   )
print(param_2)