class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            bucket = set()
            for num in row:
                if num != '.':
                    if num in bucket:
                        return False
                    bucket.add(num)
        for i in range(len(board[0])):
            bucket = set()
            for j in range(len(board)):
                if board[j][i] != '.':
                    if board[j][i] in bucket:
                        return False
                    bucket.add(board[j][i])
        for i in range(len(board)):
            if i % 3 == 0:
                buckets = [set() for _ in range(3)]
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in buckets[j//3]:
                        return False
                    buckets[j//3].add(board[i][j])
        return True
