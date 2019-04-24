import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(c):
   c.sort(reverse=True)
   print(c)
   totalsum = 0
   for j in range(len(c)):
       print(c[j])
       totalsum += (pow(2,j)*c[j])
   return totalsum

if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

   n = int(input())

   calorie = list(map(int, input().rstrip().split()))

   result = marcsCakewalk(calorie)

   fptr.write(str(result) + '\n')

   fptr.close()

