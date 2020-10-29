x, y, n = input().split()
x = int(x)
y = int(y)
n = int(n)

nums = []

for i in range(n):
  newN = i+1
  nums.append(newN)
for i in nums:
  if i%x == 0 and i%y == 0:
    print ("FizzBuzz")
  elif i%x == 0:
    print ("Fizz")
  elif i%y == 0:
    print ("Buzz")
  else:
    print (i)
