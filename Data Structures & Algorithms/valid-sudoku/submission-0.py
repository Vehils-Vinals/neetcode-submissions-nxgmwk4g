class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_column = defaultdict(set)
        seen_case = defaultdict(set)
        for i in range(9):
            seen_lign = set()
            for j in range(9):
                elt = board[i][j]
                if elt == '.':
                    continue
                if (elt in seen_lign or
                        elt in seen_column[j] or
                        elt in seen_case[(i//3, j//3)]):
                    return False
                seen_column[j].add(elt)
                seen_lign.add(elt)
                seen_case[(i//3, j//3)].add(elt)
        return True     