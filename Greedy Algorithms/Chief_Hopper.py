import math
import os
import random
import re
import sys
def chiefHopper(arr):
   s, p = 0, 2.0
   for i in range(len(arr)):
       s += arr[i] / p
       p *= 2

   attempt = int(math.ceil(s))
   start = attempt
   for i in arr:
       start = 2 * start - i
       if start < 0:
           attempt += 1
           break

   return attempt

if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

   n = int(input())

   arr = list(map(int, input().rstrip().split()))

   result = chiefHopper(arr)

   fptr.write(str(result) + '\n')

   fptr.close()
