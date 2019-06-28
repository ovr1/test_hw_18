def validate_board(board):
   count_1=0
   count_2=0
   n = [0,1,2]
   N = []
   if len(board)!=3:
       return False
   for line in board:
       count_1 += line.count(1)
       count_2 += line.count(2)
       if len(line) != 3:
           N.append(0)
       #if (line.count(1)==line.count(2)) or (line.count(1) - line.count(2) == 1):
       #    N.append(1)
       #else:
       #    N.append(0)
       for x in line:
           if x in n:
               N.append(1)
           else:
               N.append(0)
   if 0 in N:
        return False
   else:
       return True

def game_finished(board):

   count_1=0
   count_2=0
   N = []
   L =[]
   for line in board:
       count_1 += line.count(1)
       count_2 += line.count(2)
       if validate_board(board) == False:
           print(False)
           break
       if line.count(1)== 3:
           N.append(1)
       elif line.count(2)== 3:
           N.append(2)
       elif (line.count(1)+line.count(2)):
           L.append((line.count(1)+line.count(2)))
       else:
           N.append(-1)
   if sum(L)<=6:
       N.append(0)
   if 1 in N:
       return int(1)
   elif 2 in N:
       return int(2)
   elif 0 in N:
       return int(0)
   else:
       return int(-1)

b = [[1, 2, 0], [2, 2, 1 ], [1, 2, 0]]

print(game_finished(b))
