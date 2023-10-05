class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])

        count = 1  # Initialize count to 1 for the first interval
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                # Non-overlapping interval found
                count += 1
                end = intervals[i][1]

        # Calculate the number of intervals to remove
        to_remove = len(intervals) - count
        return to_remove
            
            