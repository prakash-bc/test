import heapq
def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    res = []
    for x, y in points:
        dist = x**2+y**2
        res.append((dist, x, y))
    print(res)
    heapq.heapify(res)
    results = []
    for iii in range(k):
        print(iii)
        results.append(heapq.heappop(res))
    print(results)

# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
points = [[1,3],[-2,2]]
k = 1
kClosest(points, k)