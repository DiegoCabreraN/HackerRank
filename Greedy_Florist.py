import math
import os
import random
import re
import sys
 
def getMinimumCost(k, c):
   ans = 0

   c.sort(reverse = True)
  
   cnt = 0
  
   for i in range(len(c)):
       ans += (c[i] * (cnt//k+1))
       cnt += 1
   return ans

if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

   nk = input().split()

   n = int(nk[0])

   k = int(nk[1])

   c = list(map(int, input().rstrip().split()))

   minimumCost = getMinimumCost(k, c)

   fptr.write(str(minimumCost) + '\n')

   fptr.close()

