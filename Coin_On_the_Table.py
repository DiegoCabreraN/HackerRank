import os
import sys
import math 
def coinOnTheTable(n, m, K, board):
   x = 0
   y = 0  
   for i in range(n):
       for j in range(m):
           if(board[i][j]=='*'):
               x = i
               y = j
   ans = 10000
   N = []
   L = [[0 for i in range(52)] for j in range(52)]
   for k in range(K+1): 
       M = [[0 for i in range(52)] for j in range(52)]
       for i in range(n): 
           for j in range(m): 
               if(k==0): 
                   if(i == 0 and j == 0):
                       M[0][0] = 0  
                   else:
                       M[i][j] = 10000
               else: 
                   res = math.inf 
                   if(i>0):
                       if(board[i-1][j] == 'D'): 
                           res = min(res,L[i-1][j]) 
                       else: 
                           res = min(res,L[i-1][j]+1)
                   if(i<(n-1)): 
                       if(board[i+1][j] == 'U'): 
                           res = min(res,L[i+1][j])
                       else:  
                           res = min(res,L[i+1][j]+1)
                   if(j>0):
                       if(board[i][j-1] == 'R'): 
                           res = min(res,L[i][j-1])
                       else: 
                           res = min(res,L[i][j-1]+1) 

                   if(j<(m-1)):
                       if(board[i][j+1] == 'L'): 
                           res = min(res,L[i][j+1])
                       else:
                           res = min(res,L[i][j+1]+1)  
                   M[i].insert(j,res)
                   M[i].pop(j+1)
       L = M
       N.insert(k,L)
       print("K"+str(k))
       print(L)  
   for k in range(K+1):
       ans = min(ans,N[k][x][y])

   if(ans < 10000):
       return ans
   else:
       return -1 

if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w') 
   nmk = input().split() 
   n = int(nmk[0]) 
   m = int(nmk[1])
   k = int(nmk[2])  
   board = []
   for _ in range(n):
       board_item = input()
       board.append(board_item)
   result = coinOnTheTable(n, m, k, board)
   fptr.write(str(result) + '\n')
   fptr.close()
