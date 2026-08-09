# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the
# non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(len(intervals)):
            # Check if lower range element in current subarray is <= upper range element in last subarray

            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result


soln = Solution()

intervals = [[1,4],[0,2],[3,5]]

print(soln.merge(intervals))