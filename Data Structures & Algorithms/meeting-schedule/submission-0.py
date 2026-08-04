"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda interval: interval.start)
        prev_end = intervals[0].end

        for meeting in intervals[1:]:
            start = meeting.start
            end = meeting.end
            if prev_end > start:
                return False
            
            prev_end = end
        
        return True