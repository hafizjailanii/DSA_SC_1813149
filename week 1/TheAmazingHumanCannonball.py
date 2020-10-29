import math

n = int(input())

for i in range(n):
  v, a, x, b, t = input().split()
  v = float(v)
  a = float(a)
  x = float(x)
  b = float(b)
  t = float(t)
  time = (x/(v*math.cos((a*(math.pi/180)))))
  y = ((v*time*math.sin((a*(math.pi/180))))-((1/2)*9.81*(time**2)))
  if (y >= b+1 and y <= t-1):
    print ("Safe")
  else:
    print ("Not Safe")
