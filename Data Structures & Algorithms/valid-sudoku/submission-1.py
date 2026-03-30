class Solution:
    def check_line_columns(self, liste, i):
        seen_line, seen_columns = set(), set()

        for j in range(9):
            if liste[i][j] != "." and liste[i][j] in seen_line:
                return False
            seen_line.add(liste[i][j])
            if liste[j][i] != "." and liste[j][i] in seen_columns:
                return False
            seen_columns.add(liste[j][i])
        return True

    def check_square(self, liste, i, j):
        seen = set()
        for k in range(3):
            for c in range(3):
                if (liste[k + i][c + j] != "." and
                liste[k + i][c + j] in seen):
                    return False
                seen.add(liste[k + i][c + j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Val = True
        for i in range(9):
            Val *= self.check_line_columns(board, i)
        print(Val)
        for i in range(3):
            for j in range(3):
                Val *= self.check_square(board, i*3, j*3)
        return Val==1
        