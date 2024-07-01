import heapq
def lastStoneWeight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    print(stones)

    for i, s in enumerate(stones):
        stones[i] = -s
    print(stones)

    heapq.heapify(stones)
    print(stones)
    # first, second =  heapq.heappop(stones), heapq.heappop(stones)
    # print(first, second)
    # print(-first, -second)


    while len(stones)>1:
        first, second =  heapq.heappop(stones), heapq.heappop(stones)
        print(stones, "stones")

        if first < second:
            print("MERGE DIFF", first, second)
            heapq.heappush(stones,first-second)
        else:
            print("MERGE ", first, second)

    stones.append(0)
    print(stones)


    # stones = [-s for s in stones]
    # print(stones)
    # print(heapq.heapify(stones))
    # print(stones)
    # print(type(stones))
    # print(heapq.heappop(stones))

    # while len(stones)>1:
    #     first, second = heapq.heappop(stones), heapq.heappop(stones)
    #     if first< second:
    #         heapq.heappush(stones, abs(second-first))
    # print(stones)




        
stones = [2,7,4,1,8,1]

lastStoneWeight(stones)
# Input: stones = [2,7,4,1,8,1]
# Output: 1