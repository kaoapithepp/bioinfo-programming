# ACTUAL INPUT FROM USER
"""
    GET RID THE COMMENT AFTER THE SYSTEM WORKS PROPERLY.
"""
seq1 = "-" + input("Enter your 1st sequence: ")
seq2 = "-" + input("Enter your 2nd sequence: ")
match_bonus = int(input("Enter Match bonus: "))
mismatch_penalty = int(input("Enter Mismatch: "))
gap_penalty = int(input("Enter Gap: "))


# FOR TESTING ONLY : dummy data
# seq1 = "-GCATGCTA"
# seq2 = "-GATTACCA"
# match_bonus = 5
# mismatch_penalty = -1
# gap_penalty = -2

# GLOBAL CONSTANT VARAIBLES
n_rows = len(seq1)
n_cols = len(seq2)

# generate scoreboard as 2D array
score_board = []
for i in range(n_rows):
    col = []
    for j in range(n_cols):
        col.append(0)
    score_board.append(col)

# FOR TESTING ONLY : generate placeholder number to table
# count = 0
# for row_index in range(n_rows):
#     for col_index in range(n_cols):
#         score_board[row_index][col_index] = count
#         count += 1


# Needleman Wunsch alignment
for row in range(n_rows):
    for col in range(n_cols):        
        if row == 0 and col == 0:
            score = 0

        elif row == 0:
            previous_score = score_board[row][col - 1]
            score = previous_score + gap_penalty

        elif col == 0:
            previous_score = score_board[row -1][col]
            score = previous_score + gap_penalty

        else: 
            cell_to_the_left = score_board[row][col-1]
            from_left_score = cell_to_the_left + gap_penalty
             
            above_cell = score_board[row-1][col]
            from_above_score = above_cell + gap_penalty
            
            diagonal_left_cell = score_board[row-1][col-1]
            
            if seq1[row-1] == seq2[col-1]:
                diagonal_left_cell_score = diagonal_left_cell + match_bonus
            else:
                diagonal_left_cell_score = diagonal_left_cell + mismatch_penalty
            
            score = max([from_left_score,from_above_score,diagonal_left_cell_score])

        score_board[row][col] = score

# generate pretty display
def displayView():
    format_row = "{:>12}" * (n_rows + 1)
    print(format_row.format("", *seq1))
    for v, row in zip(seq2, score_board):
        print(format_row.format(v, *row))

# DON'T TOUCH : display section
displayView()