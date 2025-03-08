class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R = C = 9

        for i in range(R):
            occ_x = set()
            occ_y = set()
            for j in range(C):
                num_x = board[i][j]
                num_y = board[j][i]
                if num_x != '.' and num_x in occ_x:
                    return False
                if num_y != '.' and num_y in occ_y:
                    return False
                occ_x.add(num_x)
                occ_y.add(num_y)

                if i % 3 == 0 and j % 3 == 0:
                    occ = set()
                    for x in range(R // 3):
                        for y in range(C // 3):
                            num = board[i + x][j + y]
                            if num != '.' and num in occ:
                                return False
                            occ.add(num)

        return True

"""Interesting Solution"""
# def isValidSudoku(self, board: List[List[str]]) -> bool:
# 	s = set()

# 	for i in range(9):
# 		for j in range(9):
# 			if board[i][j] != '.':
# 				c = board[i][j]

# 				# Row check
# 				key = f'{c} in row {i}' # same as -> str(c) + ' in row ' + str(i)

# 				if key in s:
# 					return False
# 				else:
# 					s.add(key)

# 				# Column check
# 				key = f'{c} in col {j}' # same as -> str(c) + ' in col ' + str(j)

# 				if key in s:
# 					return False
# 				else:
# 					s.add(key)

# 				# Box check
# 				boxIndex = (i // 3) * 3 + (j // 3)
# 				key = f'{c} in box {boxIndex}' # same as -> str(c) + ' in box ' + str(boxIndex)

# 				if key in s:
# 					return False
# 				else:
# 					s.add(key) 

# 	return True