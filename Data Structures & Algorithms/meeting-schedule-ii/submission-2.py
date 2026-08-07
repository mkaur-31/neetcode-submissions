"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # stack =[]
        
        # intervals.sort(key=lambda x: x.start)
        # for interval in intervals:
        #     if stack and stack[0] <= interval.start:
        #         heapq.heappop(stack)
        #     heapq.heappush(stack, interval.end)
        # return len(stack)
        mp = defaultdict(int)
        for i in intervals:
            mp[i.start] += 1
            mp[i.end] -= 1
        prev , res =0,0
        for key in sorted(mp.keys()):
            prev += mp[key]
            res = max(res,prev)
        return res



        