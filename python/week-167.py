# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

# You are given a directed graph of n nodes numbered from 0 to n - 1, where
# each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n,
# indicating that there is a directed edge from node i to node edges[i].
# If there is no outgoing edge from i, then edges[i] == -1.

# You are also given two integers node1 and node2.

# Return the index of the node that can be reached from both node1 and node2,
# such that the maximum between the distance from node1 to that node, and from
# node2 to that node is minimized. If there are multiple answers, return the
# node with the smallest index, and if no possible answer exists, return -1.

# Note that edges may contain cycles.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) ->int:
        node1_distances = {}
        node2_distances = {}

        node1_distance = 0
        node2_distance = 0

        length = len(edges)
        best_node = -1

        i = node1
        j = node2

        best_score = float("inf")

        while i != -1 and i not in node1_distances:
            node1_distances[i] = node1_distance # Record distance
            i = edges[i] # Point to next node in the chain
            node1_distance += 1 # Increment each distance by step

        while j != -1 and j not in node2_distances:
            node2_distances[j] = node2_distance
            j = edges[j]
            node2_distance += 1

        for i in range(0, length):
            # Check if node has been traversed by both nodes
            if i in node1_distances and i in node2_distances:
                # Take their maximum distances
                score = max(node1_distances[i], node2_distances[i])

                # If better score is achieved, record the score along with
                # the index of the node
                if score < best_score:
                    best_score = min(best_score, score)
                    best_node = i

        return best_node

soln = Solution()

edges = [2,2,3,-1]
node1 = 0
node2 = 1

print(soln.closestMeetingNode(edges, node1, node2))
