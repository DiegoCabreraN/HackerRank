n, h, i = input().split()
n = int(n)
h = int(h)
i = int(i)
b = [[0 for j in range(0, h)] for j in range(0, n)]

for k in range(0, n):
   l = input().split()
   for m in range(0, int(l[0])):
       b[k][int(l[m + 1]) - 1] += 1

for level in range(0, h):
   if level > 0:
       twoprev = 0 
       if level >= i:                                     
           for j in range(0, n):
               if b[j][level - i] > twoprev:
                   twoprev = b[j][level - i]          
       for j in range(0, n):
           if level >= i and b[j][level - 1] < twoprev:
               b[j][level] += twoprev
           else:
               b[j][level] += b[j][level - 1]

absmax = 0
for j in range(0, n):
   if absmax < b[j][h - 1]:
       absmax = b[j][h - 1]
print(absmax)
