N = []
n = [0, 1, 2]

def validate_board(board):
    if(check_ryd(board) is True and check_line(board) is True and check_right(board)is True and check_task(board) is True):
        return True
    else:
        return False

def check_ryd(board):
    if len(board)==3:
        return True
    else:
        return False

def check_line(board):
    for line in board:
        if len(line) == 3:
            return True
        else:
            return False

def check_right(board):
    for line in board:
        for x in line:
            if x in n:
                continue
            else:
                return False
    return True

def check_task(board):
    count_1 = 0
    count_2 = 0
    count_0 = 0
    for line in board:
        count_1 += line.count(1)
        count_2 += line.count(2)
        count_0 += line.count(0)
        if ((line.count(1) == line.count(2))and line.count(0) != 3) or ((line.count(1) - line.count(2) == 1 )and line.count(0) != 3) :
            continue
        else:
            return False
    return True








board = [[0, 2,  1], [0, 2, 1], [1, 1, 2]]
print(validate_board(board))

