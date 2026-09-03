class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        res = []


        for i in range(len(intervals)):
            st, end = intervals[i]
            if ne < st:
                res.append(newInterval)
                return res + intervals[i:]
            elif ns > end:
                res.append(intervals[i])
            else:
                ns = min(ns,st)
                ne = max(ne,end)
                newInterval = [ns,ne]
        res.append(newInterval)
        return res
        