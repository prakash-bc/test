
class Solution(object):
   
    def carFleet(self, target, position, speed):
        pairs = [(p, s) for p, s in zip(position, speed) ]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            stack.append((target-p)//s)
            if len(stack)>=2 and stack[-1]<= stack[-2]:
                stack.pop()
        print(stack, len(stack))
        return len(stack)

    def carFleet2(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            t = (target - p) / s
            stack.append(t)
            print(t, p, s)
            # t = (target - p) / s
            # if len(stack)==0  or t>stack[-1]:
            #     stack.append(t)
        print(stack)
        return len(stack)
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]  

# target=10
# position = [6,8]
# speed=[3,2]
Solution().carFleet2(target, position, speed)