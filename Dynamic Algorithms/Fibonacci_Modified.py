import math
import os
import random
import re
import sys
 
arr = []
def fibonacciModified(t1, t2, n):
   arr = [None]*(n+1)
   arr[0] = t1
   arr[1] = t2
   while arr[n-1] == None:
       for i in range(2,n):
           arr[i] = arr[i-2]+(arr[i-1]**2)
   return arr[n-1] 

if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

   t1T2n = input().split()

   t1 = int(t1T2n[0])

   t2 = int(t1T2n[1])

   n = int(t1T2n[2])

   result = fibonacciModified(t1, t2, n)

   fptr.write(str(result) + '\n')

   fptr.close()
