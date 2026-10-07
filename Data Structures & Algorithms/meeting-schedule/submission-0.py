"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start = []
        end = []
        for i in range(len(intervals)):
            a = intervals[i].start
            b = intervals[i].end
            start.append(a)
            end.append(b)
        for j in range(len(end)):
            for k in range(len(start) - 1):
                if j == k:
                    continue
                if start[j] < end[k] and end[j] > start[k]:
                    return False
        return True





