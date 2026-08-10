# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word,
# return true if word exists in the grid.

# The word can be constructed from letters of sequentially
# adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        seen = set()
        rows = len(board)
        cols = len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = False

        def search(coordinate, index):
            nonlocal new_word, res

            if index == len(word):
                res = True
                return

            x, y = coordinate

            for i in directions:
                new_x = x + i[0]
                new_y = y + i[1]
                new_coordinates = (new_x, new_y)

                if 0 <= new_x <= rows - 1 and 0 <= new_y <= cols - 1 and new_word != word and new_coordinates not in seen:
                    if word[index] == board[new_x][new_y]:
                        seen.add(new_coordinates)
                        search(new_coordinates, index + 1)
                        seen.remove(new_coordinates)

        for i, el in enumerate(board):
            for j, el in enumerate(board[i]):
                if board[i][j] == word[0] and (i, j) not in seen:
                    seen.add((i, j))
                    search((i, j), 1)
                    seen.clear()

        return res


soln = Solution()

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

print(soln.exist(board, word))
