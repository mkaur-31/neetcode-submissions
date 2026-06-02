class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        stack = []

        for p,s in pair:
            temp = (target-p)/s
            if not stack or temp > stack[-1]: 
                stack.append((target-p)/s)

        return len(stack)
