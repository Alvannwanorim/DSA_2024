from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if(len(intervals) == 0): return True
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0][1]

        for start,end in intervals[1:]:
            if start < prev:
                return False
            else:
                prev = end
        return True