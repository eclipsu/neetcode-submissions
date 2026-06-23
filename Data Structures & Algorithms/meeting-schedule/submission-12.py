"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i :  i.start )
        
        for i in range(1, len(intervals)):
            i_1 = intervals[i - 1]
            i_2 = intervals[i]

            if i_2.start < i_1.end:
                return False
            
        return True