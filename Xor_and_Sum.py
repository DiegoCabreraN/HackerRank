import os
import sys 

def xorAndSum(a, b):
   a10 = int(a,2)
   b10 = int(b,2)
   sum = 0
   for i in range(0,314160):
       sum += (a10 ^ (b10 << i))
   return (sum % 1000000007)

if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

   a = input()

   b = input()

   result = xorAndSum(a, b)

   fptr.write(str(result) + '\n')

   fptr.close()
