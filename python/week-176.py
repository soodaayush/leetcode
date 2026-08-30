# https://leetcode.com/problems/interval-list-intersections/

# You are given two lists of closed intervals, firstList and secondList,
# where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
# Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with
# a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are
# either empty or represented as a closed interval. For example, the
# intersection of [1, 3] and [2, 4] is [2, 3].

# Time Complexity: O(N + M), N = # of A intervals, M = # of B intervals
# Space Complexity: O(1)

class Solution:
    def intervalIntersection(self, firstList: list[list[int]],secondList: list[list[int]]) -> list[list[int]]:
        a = 0
        b = 0
        a_len = len(firstList)
        b_len = len(secondList)
        intervals = []

        while a < a_len and b < b_len:
            # FirstList: [a[0], a[1]], SecondList: [b[0], b[1]]
            # Example: FirstList: [0, 2], secondList: [1, 5]
            # New Interval: [max(a[0], b[0]), min(a[1], b[1])] = [1, 2]

            if (secondList[b][0] <= firstList[a][1] and firstList[a][0] <=
                    secondList[b][1]):
                intervals.append([max(firstList[a][0], secondList[b][0]),
                                  min(firstList[a][1], secondList[b][1])])

            # If interval is finished, move either pointer depending on the case

            if firstList[a][1] < secondList[b][1]:
                a += 1
            elif secondList[b][1] < firstList[a][1]:
                b += 1
            else:
                a += 1
                b += 1

        return intervals

soln = Solution()

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

print(soln.intervalIntersection(firstList, secondList))
