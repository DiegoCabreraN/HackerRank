import math
import os
import random
import re
import sys
 
def minimumAbsoluteDifference(arr): 
   minimum = math.inf
   arr = sorted(arr)  
   for i in range(n-1):
       if arr[i+1] - arr[i] < minimum:
           minimum = arr[i+1] - arr[i] 
   return minimum

if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

   n = int(input())

   arr = list(map(int, input().rstrip().split()))

   result = minimumAbsoluteDifference(arr)

   fptr.write(str(result) + '\n')

   fptr.close()
