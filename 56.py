class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        sorted_intervals = sorted(intervals)
        condensed = [sorted_intervals[0]]
        for start, end in sorted_intervals[1:]:
            if start > condensed[-1][1]:
                condensed.append([start, end])
            else:
                old_start, old_end = condensed.pop()
                condensed.append([old_start, max(old_end, end)])
                
        return condensed
